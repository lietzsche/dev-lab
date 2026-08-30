"""DearPyGui 기반 GUI. 러스트판 PortKeeper와 같은 구조를 따른다:
상단 툴바 + 왼쪽 터널 목록 + 오른쪽 로그 패널, 그리고 추가/편집·인증 정보
입력을 위한 모달 창.
"""
from __future__ import annotations

import queue
import time
import uuid
from pathlib import Path
from typing import Optional

import dearpygui.dearpygui as dpg

from . import config
from .config import AppConfig, AuthKind, TunnelProfile
from .tunnel import PasswordCredentials, PrivateKeyCredentials, StatusEvent, TunnelManager

ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets"
MAX_LOG_LINES = 500

AUTH_PASSWORD_LABEL = "비밀번호"
AUTH_KEY_LABEL = "개인 키 (PEM/OpenSSH)"


def _status_label(status: StatusEvent) -> str:
    if status.kind == "stopped":
        return "중지됨"
    if status.kind == "connecting":
        return "연결 중..."
    if status.kind == "connected":
        since = status.fields["since"]
        active = status.fields["active_connections"]
        elapsed = max(0, int(time.monotonic() - since))
        h, rem = divmod(elapsed, 3600)
        m, s = divmod(rem, 60)
        return f"연결됨 · {h:02d}:{m:02d}:{s:02d} 경과 · 활성 연결 {active}개"
    if status.kind == "reconnecting":
        attempt = status.fields["attempt"]
        retry_in = int(status.fields["retry_in"])
        return f"재연결 대기 중 (시도 {attempt}회, {retry_in}초 후)"
    if status.kind == "error":
        return f"오류: {status.fields['message']}"
    return status.kind


def _status_color(status: StatusEvent) -> tuple[int, int, int, int]:
    if status.kind == "connected":
        return (46, 160, 67, 255)
    if status.kind == "error":
        return (220, 53, 69, 255)
    if status.kind == "stopped":
        return (150, 150, 150, 255)
    return (255, 193, 7, 255)


class PortKeeperApp:
    def __init__(self) -> None:
        self.config: AppConfig = config.load()
        self.manager = TunnelManager()
        self.known_hosts_path = config.known_hosts_path()
        self.log_queue: "queue.Queue[str]" = queue.Queue()
        self.session_creds: dict[str, object] = {}
        self._log_item_tags: list[int] = []
        self._editor_profile_id: Optional[str] = None
        self._pending_profile_id: Optional[str] = None
        self._korean_font = None

    # ---- 조회 도우미 -----------------------------------------------------

    def _find_profile(self, profile_id: str) -> Optional[TunnelProfile]:
        return next((p for p in self.config.profiles if p.id == profile_id), None)

    # ---- 실행 -------------------------------------------------------------

    def run(self) -> None:
        dpg.create_context()
        self._setup_fonts()
        self._build_ui()
        self._rebuild_profile_list()
        self._auto_start()

        dpg.create_viewport(title="PortKeeper (Python)", width=1000, height=650, min_width=760, min_height=480)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("main_window", True)

        try:
            while dpg.is_dearpygui_running():
                self._poll()
                dpg.render_dearpygui_frame()
        finally:
            self.manager.stop_all()
            dpg.destroy_context()

    def _setup_fonts(self) -> None:
        font_path = str(ASSETS_DIR / "fonts" / "NanumGothic-Regular.ttf")
        with dpg.font_registry():
            with dpg.font(font_path, 18) as korean_font:
                self._korean_font = korean_font
        dpg.bind_font(self._korean_font)

    def _auto_start(self) -> None:
        # 자동 시작은 비밀번호 입력이 필요 없는 "패스프레이즈 없는 키" 프로필에서만
        # 조용히 진행한다. 비밀번호 인증은 항상 사용자 확인을 거친다.
        for profile in self.config.profiles:
            if profile.auto_start and profile.auth.is_private_key:
                creds = PrivateKeyCredentials(key_path=profile.auth.key_path, passphrase=None)
                self._start_with_credentials(profile, creds)

    # ---- 매 프레임 폴링 -----------------------------------------------------

    def _poll(self) -> None:
        while True:
            try:
                line = self.log_queue.get_nowait()
            except queue.Empty:
                break
            self._append_log(line)

        self.manager.poll()
        for profile in self.config.profiles:
            self._refresh_row_status(profile)

    def _refresh_row_status(self, profile: TunnelProfile) -> None:
        pid = profile.id
        status_tag = f"status_{pid}"
        if not dpg.does_item_exist(status_tag):
            return
        status = self.manager.status(pid)
        dpg.set_value(status_tag, _status_label(status))
        dpg.configure_item(f"dot_{pid}", color=_status_color(status))
        running = self.manager.is_running(pid)
        dpg.configure_item(f"startstop_{pid}", label="중지" if running else "시작")

    def _append_log(self, line: str) -> None:
        tag = dpg.add_text(line, parent="log_window", wrap=0)
        self._log_item_tags.append(tag)
        if len(self._log_item_tags) > MAX_LOG_LINES:
            old = self._log_item_tags.pop(0)
            if dpg.does_item_exist(old):
                dpg.delete_item(old)
        try:
            dpg.set_y_scroll("log_window", dpg.get_y_scroll_max("log_window"))
        except Exception:  # noqa: BLE001 - 스크롤 실패는 무시해도 안전하다
            pass

    def _clear_logs(self) -> None:
        for tag in self._log_item_tags:
            if dpg.does_item_exist(tag):
                dpg.delete_item(tag)
        self._log_item_tags.clear()

    # ---- UI 구성 ------------------------------------------------------------

    def _build_ui(self) -> None:
        with dpg.window(tag="main_window"):
            with dpg.group(horizontal=True):
                dpg.add_text("PortKeeper (Python)")
                dpg.add_text("SSH 로컬 포트 포워딩 도구")
                dpg.add_spacer(width=12)
                dpg.add_button(label="+ 새 터널 추가", callback=lambda s, a, u: self._open_editor(None))
                dpg.add_button(label="모두 중지", callback=lambda s, a, u: self.manager.stop_all())
            dpg.add_separator()
            with dpg.group(horizontal=True):
                with dpg.child_window(tag="profile_list_window", width=380, height=-1, border=True):
                    pass
                with dpg.group(width=-1):
                    with dpg.group(horizontal=True):
                        dpg.add_text("로그")
                        dpg.add_button(label="지우기", callback=lambda s, a, u: self._clear_logs())
                    with dpg.child_window(tag="log_window", width=-1, height=-1, border=True):
                        pass

        self._build_editor_window()
        self._build_auth_window()

    def _build_editor_window(self) -> None:
        with dpg.file_dialog(
            directory_selector=False,
            show=False,
            callback=self._on_key_file_selected,
            tag="key_file_dialog",
            width=600,
            height=400,
        ):
            dpg.add_file_extension(".*")

        with dpg.window(
            label="새 터널 추가",
            modal=True,
            show=False,
            tag="editor_window",
            width=460,
            no_resize=True,
            no_collapse=True,
        ):
            dpg.add_input_text(label="이름", tag="editor_name")
            dpg.add_input_text(label="SSH 호스트", tag="editor_host")
            dpg.add_input_int(label="SSH 포트", tag="editor_port", min_value=1, max_value=65535, min_clamped=True, max_clamped=True)
            dpg.add_input_text(label="사용자 이름", tag="editor_user")
            dpg.add_radio_button(
                (AUTH_PASSWORD_LABEL, AUTH_KEY_LABEL),
                tag="editor_auth",
                horizontal=True,
                callback=self._on_auth_radio_changed,
            )
            with dpg.group(tag="editor_key_group", show=False):
                dpg.add_input_text(label="개인 키 파일 경로", tag="editor_key_path")
                dpg.add_button(label="찾아보기...", callback=lambda s, a, u: dpg.show_item("key_file_dialog"))
            dpg.add_input_text(label="로컬 바인드 주소", tag="editor_local_bind")
            dpg.add_input_int(label="로컬 포트", tag="editor_local_port", min_value=1, max_value=65535, min_clamped=True, max_clamped=True)
            dpg.add_input_text(label="원격 호스트 (SSH 서버 기준)", tag="editor_remote_host")
            dpg.add_input_int(label="원격 포트", tag="editor_remote_port", min_value=1, max_value=65535, min_clamped=True, max_clamped=True)
            dpg.add_checkbox(label="앱 실행 시 자동 시작", tag="editor_autostart")
            dpg.add_checkbox(label="새 호스트 키 자동 신뢰 (TOFU)", tag="editor_tofu")
            dpg.add_separator()
            with dpg.group(horizontal=True):
                dpg.add_button(label="저장", callback=self._on_save_profile)
                dpg.add_button(label="취소", callback=lambda s, a, u: dpg.hide_item("editor_window"))

    def _build_auth_window(self) -> None:
        with dpg.window(
            label="인증 정보 입력",
            modal=True,
            show=False,
            tag="auth_window",
            width=420,
            no_resize=True,
            no_collapse=True,
        ):
            dpg.add_text("", tag="auth_prompt_text")
            dpg.add_text("", tag="auth_label_text")
            dpg.add_input_text(password=True, tag="auth_secret")
            dpg.add_checkbox(label="이번 세션 동안 기억하기 (재연결 시 다시 묻지 않음)", tag="auth_remember", default_value=True)
            dpg.add_separator()
            with dpg.group(horizontal=True):
                dpg.add_button(label="연결", callback=self._on_confirm_auth)
                dpg.add_button(label="취소", callback=lambda s, a, u: dpg.hide_item("auth_window"))

    def _rebuild_profile_list(self) -> None:
        dpg.delete_item("profile_list_window", children_only=True)
        if not self.config.profiles:
            dpg.add_text(
                '등록된 터널이 없습니다.\n위의 "+ 새 터널 추가" 버튼으로 시작하세요.',
                parent="profile_list_window",
                wrap=340,
            )
            return
        for profile in self.config.profiles:
            self._add_profile_row(profile)

    def _add_profile_row(self, profile: TunnelProfile) -> None:
        pid = profile.id
        with dpg.group(parent="profile_list_window"):
            with dpg.child_window(height=150, border=True):
                with dpg.group(horizontal=True):
                    dpg.add_text("●", tag=f"dot_{pid}", color=(150, 150, 150, 255))
                    dpg.add_text(profile.name)
                dpg.add_text(
                    f"로컬 {profile.local_bind}:{profile.local_port}  ->  "
                    f"(SSH {profile.username}@{profile.ssh_host}:{profile.ssh_port})  ->  "
                    f"{profile.remote_host}:{profile.remote_port}",
                    wrap=340,
                )
                dpg.add_text("중지됨", tag=f"status_{pid}")
                with dpg.group(horizontal=True):
                    dpg.add_button(label="시작", tag=f"startstop_{pid}", callback=self._on_start_stop, user_data=pid)
                    dpg.add_button(label="편집", callback=self._on_edit, user_data=pid)
                    dpg.add_button(label="삭제", callback=self._on_delete, user_data=pid)
            dpg.add_spacer(height=4)

    # ---- 콜백 ----------------------------------------------------------------

    def _on_start_stop(self, sender, app_data, user_data) -> None:
        profile_id = user_data
        if self.manager.is_running(profile_id):
            self.manager.stop(profile_id)
        else:
            self._request_start(profile_id)

    def _on_edit(self, sender, app_data, user_data) -> None:
        profile = self._find_profile(user_data)
        if profile is not None:
            self._open_editor(profile)

    def _on_delete(self, sender, app_data, user_data) -> None:
        profile_id = user_data
        self.manager.stop(profile_id)
        self.session_creds.pop(profile_id, None)
        self.config.profiles = [p for p in self.config.profiles if p.id != profile_id]
        config.save(self.config)
        self._rebuild_profile_list()

    def _on_auth_radio_changed(self, sender, app_data, user_data) -> None:
        dpg.configure_item("editor_key_group", show=(app_data == AUTH_KEY_LABEL))

    def _on_key_file_selected(self, sender, app_data, user_data) -> None:
        path = ""
        if isinstance(app_data, dict):
            path = app_data.get("file_path_name") or ""
            if not path:
                selections = app_data.get("selections") or {}
                if selections:
                    path = next(iter(selections.values()))
        if path:
            dpg.set_value("editor_key_path", path)

    def _open_editor(self, profile: Optional[TunnelProfile]) -> None:
        self._editor_profile_id = profile.id if profile else None
        p = profile or TunnelProfile(name="새 터널", ssh_host="", username="")

        dpg.set_value("editor_name", p.name)
        dpg.set_value("editor_host", p.ssh_host)
        dpg.set_value("editor_port", p.ssh_port)
        dpg.set_value("editor_user", p.username)
        is_key = p.auth.is_private_key
        dpg.set_value("editor_auth", AUTH_KEY_LABEL if is_key else AUTH_PASSWORD_LABEL)
        dpg.set_value("editor_key_path", p.auth.key_path)
        dpg.configure_item("editor_key_group", show=is_key)
        dpg.set_value("editor_local_bind", p.local_bind)
        dpg.set_value("editor_local_port", p.local_port)
        dpg.set_value("editor_remote_host", p.remote_host)
        dpg.set_value("editor_remote_port", p.remote_port)
        dpg.set_value("editor_autostart", p.auto_start)
        dpg.set_value("editor_tofu", p.trust_on_first_use)
        dpg.configure_item("editor_window", label="터널 편집" if profile else "새 터널 추가")
        dpg.show_item("editor_window")

    def _on_save_profile(self, sender, app_data, user_data) -> None:
        is_key = dpg.get_value("editor_auth") == AUTH_KEY_LABEL
        auth = AuthKind.private_key(dpg.get_value("editor_key_path")) if is_key else AuthKind.password()
        profile_id = self._editor_profile_id or uuid.uuid4().hex

        profile = TunnelProfile(
            id=profile_id,
            name=dpg.get_value("editor_name") or "새 터널",
            ssh_host=dpg.get_value("editor_host"),
            ssh_port=int(dpg.get_value("editor_port")),
            username=dpg.get_value("editor_user"),
            auth=auth,
            local_bind=dpg.get_value("editor_local_bind"),
            local_port=int(dpg.get_value("editor_local_port")),
            remote_host=dpg.get_value("editor_remote_host"),
            remote_port=int(dpg.get_value("editor_remote_port")),
            auto_start=dpg.get_value("editor_autostart"),
            trust_on_first_use=dpg.get_value("editor_tofu"),
        )

        existing_index = next((i for i, p in enumerate(self.config.profiles) if p.id == profile_id), None)
        if existing_index is not None:
            self.config.profiles[existing_index] = profile
        else:
            self.config.profiles.append(profile)

        config.save(self.config)
        dpg.hide_item("editor_window")
        self._rebuild_profile_list()

    def _request_start(self, profile_id: str) -> None:
        profile = self._find_profile(profile_id)
        if profile is None:
            return
        cached = self.session_creds.get(profile_id)
        if cached is not None:
            self._start_with_credentials(profile, cached)
            return

        self._pending_profile_id = profile_id
        is_key = profile.auth.is_private_key
        dpg.set_value("auth_prompt_text", f'"{profile.name}" 터널을 시작합니다.')
        dpg.set_value("auth_label_text", "개인 키 암호문 (없으면 비워두세요)" if is_key else "SSH 비밀번호")
        dpg.set_value("auth_secret", "")
        dpg.set_value("auth_remember", True)
        dpg.show_item("auth_window")

    def _on_confirm_auth(self, sender, app_data, user_data) -> None:
        profile_id = self._pending_profile_id
        if profile_id is None:
            return
        profile = self._find_profile(profile_id)
        if profile is None:
            return

        secret = dpg.get_value("auth_secret")
        remember = dpg.get_value("auth_remember")
        if profile.auth.is_private_key:
            creds = PrivateKeyCredentials(key_path=profile.auth.key_path, passphrase=secret or None)
        else:
            creds = PasswordCredentials(password=secret)

        if remember:
            self.session_creds[profile_id] = creds

        dpg.hide_item("auth_window")
        self._pending_profile_id = None
        self._start_with_credentials(profile, creds)

    def _start_with_credentials(self, profile: TunnelProfile, credentials) -> None:
        self.manager.start(profile, credentials, self.known_hosts_path, self.log_queue)
