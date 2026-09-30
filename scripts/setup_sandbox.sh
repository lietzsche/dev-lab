#!/usr/bin/env bash

set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
project_root="$(cd -- "${script_dir}/.." && pwd)"
marker_name=".bash-lab-sandbox"

if [ -f "${script_dir}/${marker_name}" ]; then
    raw_sandbox_dir="${script_dir}"
else
    raw_sandbox_dir="${BASH_SANDBOX_DIR:-/tmp/bash-lab-sandbox}"
fi

sandbox_dir="$(cd -- "$(dirname -- "${raw_sandbox_dir}")" && pwd)/$(basename -- "${raw_sandbox_dir}")"

assert_safe_target() {
    if [ "${sandbox_dir}" = "/" ] || [ "${sandbox_dir}" = "${project_root}" ]; then
        printf '오류: 안전하지 않은 샌드박스 경로입니다: %s\n' "${sandbox_dir}" >&2
        exit 1
    fi
}

assert_owned_sandbox() {
    assert_safe_target
    if [ ! -f "${sandbox_dir}/${marker_name}" ]; then
        printf '오류: 이 도구가 만든 샌드박스가 아닙니다: %s\n' "${sandbox_dir}" >&2
        exit 1
    fi
}

install_helpers() {
    local setup_source inspect_source
    setup_source="${script_dir}/$(basename -- "${BASH_SOURCE[0]}")"
    inspect_source="${script_dir}/inspect_context.sh"
    if [ ! -f "${inspect_source}" ]; then
        inspect_source="${project_root}/scripts/inspect_context.sh"
    fi

    if [ "${setup_source}" != "${sandbox_dir}/sandbox.sh" ]; then
        cp "${setup_source}" "${sandbox_dir}/sandbox.sh"
    fi
    if [ "${inspect_source}" != "${sandbox_dir}/inspect_context.sh" ]; then
        cp "${inspect_source}" "${sandbox_dir}/inspect_context.sh"
    fi
    chmod +x "${sandbox_dir}/sandbox.sh" "${sandbox_dir}/inspect_context.sh"
}

create_fixtures() {
    mkdir -p "${sandbox_dir}/workspace" "${sandbox_dir}/bin" "${sandbox_dir}/fixtures" "${sandbox_dir}/logs"

    printf '%s\n' alpha 'two words' '*.txt' '' omega > "${sandbox_dir}/fixtures/records.txt"
    printf '%s\n' '#!/usr/bin/env bash' \
        'printf "positional_count=%d\\n" "$#"' \
        'printf "command_name=%q\\n" "$0"' \
        'i=1' \
        'for arg in "$@"; do printf "argument[%d]=%q\\n" "$i" "$arg"; i=$((i + 1)); done' \
        > "${sandbox_dir}/bin/show-argv"
    printf '%s\n' '#!/usr/bin/env bash' \
        'printf "%s\\n" "stdout: ${1:-message}"' \
        'printf "%s\\n" "stderr: ${2:-diagnostic}" >&2' \
        'exit "${3:-0}"' \
        > "${sandbox_dir}/bin/emit-streams"
    chmod +x "${sandbox_dir}/bin/show-argv" "${sandbox_dir}/bin/emit-streams"
}

init_sandbox() {
    assert_safe_target
    if [ -d "${sandbox_dir}" ]; then
        if [ "${ALLOW_EXISTING_SANDBOX:-0}" != "1" ]; then
            printf '경고: 샌드박스가 이미 존재합니다: %s\n' "${sandbox_dir}" >&2
            printf '초기화하려면 %s reset을 실행하세요.\n' "$0" >&2
            exit 1
        fi
        assert_owned_sandbox
    else
        mkdir -p "${sandbox_dir}"
        : > "${sandbox_dir}/${marker_name}"
    fi

    create_fixtures
    install_helpers
    printf 'Bash 학습 샌드박스 준비 완료: %s\n' "${sandbox_dir}"
    printf '시작: cd %q\n' "${sandbox_dir}/workspace"
    printf '관찰: ../inspect_context.sh one "two words"\n'
}

clean_sandbox() {
    if [ ! -d "${sandbox_dir}" ]; then
        printf '삭제할 샌드박스가 없습니다: %s\n' "${sandbox_dir}"
        return
    fi
    assert_owned_sandbox
    rm -rf "${sandbox_dir}"
    printf '샌드박스 삭제 완료: %s\n' "${sandbox_dir}"
}

reset_sandbox() {
    assert_owned_sandbox
    rm -rf \
        "${sandbox_dir}/workspace" \
        "${sandbox_dir}/bin" \
        "${sandbox_dir}/fixtures" \
        "${sandbox_dir}/logs"
    ALLOW_EXISTING_SANDBOX=1 init_sandbox
}

status_sandbox() {
    assert_owned_sandbox
    printf 'sandbox=%s\n' "${sandbox_dir}"
    printf 'bash=%s\n' "${BASH_VERSION}"
    printf 'workspace=%s\n' "$(find "${sandbox_dir}/workspace" -mindepth 1 -maxdepth 1 2>/dev/null | wc -l) entries"
    printf 'helpers=%s\n' "$(find "${sandbox_dir}/bin" -mindepth 1 -maxdepth 1 2>/dev/null | wc -l) commands"
}

case "${1:-init}" in
    init) init_sandbox ;;
    clean) clean_sandbox ;;
    reset) reset_sandbox ;;
    status) status_sandbox ;;
    *)
        printf '사용법: %s {init|status|reset|clean}\n' "$0" >&2
        exit 2
        ;;
esac
