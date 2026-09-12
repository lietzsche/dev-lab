"""P7-1: path 객체와 file I/O의 경계를 관찰한다."""

from dataclasses import dataclass
from pathlib import Path
from tempfile import TemporaryDirectory


@dataclass(frozen=True)
class NoteRecord:
    title: str
    content: str


def write_note_text(path: Path, content: str) -> int:
    return path.write_text(content, encoding="utf-8")


def read_note_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_note_bytes(path: Path, payload: bytes) -> int:
    return path.write_bytes(payload)


def read_note_bytes(path: Path) -> bytes:
    return path.read_bytes()


def serialize_note(note: NoteRecord) -> str:
    return f"{note.title}\n{note.content}"


def run() -> None:
    """Run the current path and file I/O exercise."""
    print()
    print("P7-1 path와 file I/O 시작")

    note_path = Path("data") / "notes.txt"
    print(f"note path repr: {note_path!r}")
    print(f"note path type: {type(note_path)}")
    print(f"note path name: {note_path.name}")
    print(f"note path suffix: {note_path.suffix}")
    print(f"note path parent: {note_path.parent}")
    print(f"note path is absolute: {note_path.is_absolute()}")
    print(f"note path exists: {note_path.exists()}")

    current_directory = Path.cwd()
    resolved_note_path = note_path.resolve()
    print(f"current directory: {current_directory}")
    print(f"resolved note path: {resolved_note_path!r}")
    print(f"resolved note path is absolute: {resolved_note_path.is_absolute()}")
    print(
        "resolved note path parent parent == current directory: "
        f"{resolved_note_path.parent.parent == current_directory}"
    )

    content = "Python 파일"
    with TemporaryDirectory() as context:
        directory_path = Path(context)
        context_path = directory_path / "note.txt"
        length = write_note_text(context_path, content)
        text = read_note_text(context_path)
        print(f"text equal content: {text == content}")
        print(f"text length: {length}")
        print(f"note.txt exists: {context_path.exists()}")
        print(f"text repr: {text!r}")
        print(f"text type: {type(text)}")

        payload = content.encode("utf-8")
        bytes_path = directory_path / "note.bin"
        bytes_length = write_note_bytes(bytes_path, payload)
        read_payload = read_note_bytes(bytes_path)
        print(f"content length: {len(content)}")
        print(f"payload length: {len(payload)}")
        print(f"bytes length: {bytes_length}")
        print(f"read bytes repr: {read_payload!r}")
        print(f"read bytes type: {type(read_payload)}")
        print(f"payload equal read payload: {payload == read_payload}")
        print(
            f"content equal read payload decoded: {content == read_payload.decode('utf-8')}"
        )

        buffered_path = directory_path / "buffered.txt"
        with buffered_path.open("w", encoding="utf-8") as writer:
            print(f"writer type: {type(writer)}")
            write_length = writer.write(content)
            print(f"write length: {write_length}")
            before_text = buffered_path.read_text(encoding="utf-8")
            print(f"before text: {before_text}")
            print(f"before text repr: {before_text!r}")
            writer.flush()
            after_text = buffered_path.read_text(encoding="utf-8")
            print(f"after text: {after_text}")
            print(f"after text repr: {after_text!r}")
            print(f"in block writer closed: {writer.closed}")
        print(f"after block writer closed: {writer.closed}")

        target_path = directory_path / "atomic.txt"
        temporary_path = directory_path / "atomic.txt.tmp"
        with target_path.open("w", encoding="utf-8") as writer:
            writer.write("old note")
        with temporary_path.open("w", encoding="utf-8") as writer:
            writer.write("new note")
        print(f"read target path: {read_note_text(target_path)}")
        print(f"read temporary path: {read_note_text(temporary_path)}")
        old_target_inode = target_path.stat().st_ino
        temporary_inode = temporary_path.stat().st_ino
        replaced_path = temporary_path.replace(target_path)
        new_target_inode = target_path.stat().st_ino
        print(f"replaced_path == target_path: {replaced_path == target_path}")
        print(f"after change read target path: {read_note_text(target_path)}")
        print(f"temporary path exists: {temporary_path.exists()}")
        print(f"old target inode preserved: {old_target_inode == new_target_inode}")
        print(f"temporary inode moved to target: {temporary_inode == new_target_inode}")

        note = NoteRecord("File I/O", "Persistence boundary")
        serialized_note_path = directory_path / "serialized-note.txt"
        serialized_note = serialize_note(note)
        write_note_text(serialized_note_path, serialized_note)
        loaded_note_text = read_note_text(serialized_note_path)
        print(f"note type: {type(note)}")
        print(f"serialized note repr: {serialized_note!r}")
        print(f"serialized note type: {type(serialized_note)}")
        print(
            "serialized note equals loaded note text: "
            f"{serialized_note == loaded_note_text}"
        )
    print(f"temporary directory exists after context: {directory_path.exists()}")
