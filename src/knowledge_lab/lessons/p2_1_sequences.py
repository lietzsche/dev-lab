"""P2-1: sequences and slicing."""


def run() -> None:
    """Run sequence experiments added during P2-1."""
    print()
    print("Run sequence experiments added during P2-1.")

    first_title = "첫 노트"
    note_titles = [first_title, "두 번째 노트", "세 번째 노트"]
    selected_title = note_titles[0]
    print(f"note titles repr: {repr(note_titles)}")
    print(f"note titles type: {type(note_titles)}")
    print(f"note titles length: {len(note_titles)}")

    print(f"selected title: {selected_title}")
    print(f"selected title type: {type(selected_title)}")
    print(f"selected title is first title: {selected_title is first_title}")

    last_title = note_titles[-1]
    print(f"last title: {last_title}")
    print(f"last title is index 2: {last_title is note_titles[2]}")

    selected_titles = note_titles[1:3]
    print(f"all note titles: {note_titles}")
    print(f"selected titles: {selected_titles}")
    print(f"selected titles type: {type(selected_titles)}")

    print(f"selected titles is note titles: {selected_titles is note_titles}")
    print(f"selected first is original index 1: {selected_titles[0] is note_titles[1]}")

    selected_titles[0] = "수정된 두 번째 노트"
    print(f"selected titles after replacement: {selected_titles}")
    print(f"note titles after replacement: {note_titles}")

    shared_tags = ["python"]
    note_tag_groups = [shared_tags, ["rust"]]
    copied_tag_groups = note_tag_groups[:]
    copied_tag_groups[0].append("backend")
    print(f"original tag groups: {note_tag_groups}")
    print(f"copied tag groups: {copied_tag_groups}")
    print(f"shared inner tags: {copied_tag_groups[0] is note_tag_groups[0]}")

    note_summary = ("첫 노트", 3)
    print(f"note summary repr: {repr(note_summary)}")
    print(f"note summary type: {type(note_summary)}")
    print(f"summary title: {note_summary[0]}")
    print(f"summary count: {note_summary[1]}")

    bundle_tags = ["python"]
    note_bundle = ("첫 노트", bundle_tags)
    bundle_tags_before = note_bundle[1]
    note_bundle[1].append("backend")
    print(f"note bundle: {note_bundle}")
    print(f"bundle tags same object: {bundle_tags_before is note_bundle[1]}")

    summary_title, summary_count = note_summary
    print(f"unpacked title: {summary_title}")
    print(f"unpacked count: {summary_count}")
    print(f"unpacked title is summary index 0: {summary_title is note_summary[0]}")

    head_title, *remaining_titles = note_titles
    print(f"head title: {head_title}")
    print(f"remaining titles: {remaining_titles}")
    print(f"remaining titles type: {type(remaining_titles)}")
    print(f"head title is original index 0: {head_title is note_titles[0]}")
