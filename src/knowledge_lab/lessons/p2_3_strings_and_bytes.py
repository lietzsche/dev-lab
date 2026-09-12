"""P2-3: strings and bytes."""


def parse_note_payload(payload):
    """Decode a UTF-8 payload and parse a pipe-delimited note."""
    title, separator, content = payload.decode("utf-8").partition("|")
    if separator:
        return {
            "title": title,
            "content": content,
        }
    return None


def run() -> None:
    """Run string and byte experiments added during P2-3."""
    print()
    print("Run string and byte experiments added during P2-3.")

    sample = "한글"
    encoded = sample.encode("utf-8")
    print(f"sample: repr: {sample!r}, type: {type(sample)}, length: {len(sample)}")
    print(f"encoded: repr: {encoded!r}, type: {type(encoded)}, length: {len(encoded)}")

    decoded = encoded.decode("utf-8")
    print(f"decoded: repr: {decoded!r}, type: {type(decoded)}, length: {len(decoded)}")
    print(f"decoded == sample: {decoded == sample}")

    title_content = "첫 노트|문자열 parsing"
    parts = title_content.partition("|")
    print(f"parts repr: {parts!r}")
    print(f"parts type: {type(parts)}")
    title, separator, content = parts
    print(f"title: {title}, type: {type(title)}")
    print(f"separator: {separator}, type: {type(separator)}")
    print(f"content: {content}, type: {type(content)}")

    test_for_fail = "test for fail"
    no_separator_parts = test_for_fail.partition("|")
    print(f"no_separator_parts repr: {no_separator_parts!r}")
    _, fail_separator, _ = no_separator_parts
    print(f"no_separator_parts is: {bool(fail_separator)}")

    payload_for_success = "검색 노트|UTF-8 경계".encode("utf-8")
    success_parsed = parse_note_payload(payload_for_success)
    print(f"success_parsed: {success_parsed}")
    payload_for_fail = "구분자 없음".encode("utf-8")
    fail_parsed = parse_note_payload(payload_for_fail)
    print(f"fail_parsed: {fail_parsed}")
