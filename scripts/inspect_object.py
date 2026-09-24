#!/usr/bin/env python3
"""Git 저수준 객체 파일(.git/objects)의 zlib 압축을 풀고 구조를 분석하는 도구.

Git이 객체를 파일시스템에 저장하는 원형:
    zlib_compress(f"{object_type} {size}\\0{content}")
"""

from __future__ import annotations

import argparse
import hashlib
import sys
import zlib
from pathlib import Path


def parse_tree_payload(payload: bytes) -> list[tuple[str, str, str]]:
    """Tree 객체의 바이너리 페이로드를 파싱하여 (mode, name, sha1) 튜플 목록을 반환합니다."""
    entries: list[tuple[str, str, str]] = []
    idx = 0
    total_len = len(payload)

    while idx < total_len:
        null_pos = payload.find(b"\x00", idx)
        if null_pos == -1:
            break

        header = payload[idx:null_pos].decode("utf-8", errors="replace")
        mode, name = header.split(" ", 1)
        idx = null_pos + 1

        sha1_bytes = payload[idx : idx + 20]
        sha1_hex = sha1_bytes.hex()
        idx += 20

        entries.append((mode, name, sha1_hex))

    return entries


def inspect_git_object(target_path: Path) -> None:
    """주어진 .git/objects 파일의 zlib 압축을 풀고 헤더와 페이로드를 분석합니다."""
    if not target_path.exists():
        print(f"오류: 파일이 존재하지 않습니다: {target_path}", file=sys.stderr)
        sys.exit(1)

    raw_bytes = target_path.read_bytes()
    try:
        decompressed = zlib.decompress(raw_bytes)
    except zlib.error as err:
        print(f"오류: zlib 압축 해제 실패: {err}", file=sys.stderr)
        sys.exit(1)

    null_idx = decompressed.find(b"\x00")
    if null_idx == -1:
        print("오류: 올바른 Git 객체 헤더(null byte)를 찾을 수 없습니다.", file=sys.stderr)
        sys.exit(1)

    header = decompressed[:null_idx].decode("ascii", errors="replace")
    payload = decompressed[null_idx + 1 :]

    try:
        obj_type, declared_size_str = header.split(" ", 1)
        declared_size = int(declared_size_str)
    except ValueError:
        print(f"오류: 유효하지 않은 헤더 포맷: {header!r}", file=sys.stderr)
        sys.exit(1)

    actual_size = len(payload)
    calculated_sha1 = hashlib.sha1(decompressed).hexdigest()

    print("=" * 60)
    print(f" 객체 타입 (Type):       {obj_type}")
    print(f" 선언 크기 (Declared):   {declared_size} bytes")
    print(f" 실제 페이로드 (Actual): {actual_size} bytes")
    print(f" 크기 일치 여부:         {declared_size == actual_size}")
    print(f" 계산된 SHA-1 해시:      {calculated_sha1}")
    print("=" * 60)
    print("[페이로드 내용 (Payload)]\n")

    if obj_type == "tree":
        tree_entries = parse_tree_payload(payload)
        for mode, name, sha1 in tree_entries:
            print(f"  {mode:>6}  {sha1}  {name}")
    elif obj_type in ("commit", "tag"):
        print(payload.decode("utf-8", errors="replace"))
    elif obj_type == "blob":
        try:
            text = payload.decode("utf-8")
            print(text)
        except UnicodeDecodeError:
            print(f"<바이너리 데이터: {len(payload)} 바이트>")
            print(payload[:128].hex())
    else:
        print(f"<알 수 없는 객체 타입: {obj_type}>")
        print(payload[:128])


def resolve_object_file(arg: str, git_dir: Path) -> Path:
    """해시 문자열 또는 파일 경로를 바탕으로 실제 객체 파일 경로를 찾습니다."""
    path = Path(arg)
    if path.is_file():
        return path

    clean_hash = arg.strip().lower()
    if len(clean_hash) == 40:
        candidate = git_dir / "objects" / clean_hash[:2] / clean_hash[2:]
        if candidate.is_file():
            return candidate

    print(
        f"오류: 객체를 찾을 수 없습니다. 경로 또는 40자리 해시를 입력하세요: {arg}\n"
        f"검색 기준 git_dir: {git_dir.resolve()}",
        file=sys.stderr,
    )
    sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Git 저수준 객체 파일의 zlib 압축을 풀고 구조를 분석합니다."
    )
    parser.add_argument("target", help="객체 파일 경로 또는 40자리 SHA-1 해시")
    parser.add_argument(
        "--git-dir",
        default=".git",
        help="Git 디렉터리 경로 (기본값: .git)",
    )
    args = parser.parse_args()

    git_dir = Path(args.git_dir)
    target_path = resolve_object_file(args.target, git_dir)
    inspect_git_object(target_path)


if __name__ == "__main__":
    main()
