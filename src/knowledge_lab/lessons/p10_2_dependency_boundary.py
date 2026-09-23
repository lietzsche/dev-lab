"""P10-2: dependency boundary를 관찰한다."""

from collections.abc import Callable
from fastapi import Depends, FastAPI, Request
from fastapi.testclient import TestClient
from typing import Annotated

app = FastAPI()


LabelBuilder = Callable[[str, str], str]


def build_note_label(title: str, source: str) -> str:
    return f"{title} [{source}]"


def execute_label_use_case(title: str, source: str, label_builder: LabelBuilder) -> str:
    return label_builder(title, source)


def get_label_builder() -> LabelBuilder:
    return build_note_label


def get_fake_note_label(_title: str, _source: str) -> str:
    return "FAKE LABEL"


@app.get("/labels")
def get_note_label(
    request: Request,
    label_builder: Annotated[LabelBuilder, Depends(get_label_builder)],
) -> dict[str, str]:
    title = request.query_params.get("title", "")
    source = request.query_params.get("source", "")
    return {"label": execute_label_use_case(title, source, label_builder)}


def get_fake_label_builder() -> LabelBuilder:
    return get_fake_note_label


def run() -> None:
    """Run the current dependency boundary exercise."""
    print()
    print("P10-2 dependency boundary 시작")

    with TestClient(app) as client:
        response = client.get("/labels?title=Python&source=api").json()
        print(f"response: {response}")
    try:
        app.dependency_overrides[get_label_builder] = get_fake_label_builder
        with TestClient(app) as overridden_client:
            overridden_response = overridden_client.get(
                "/labels?title=Python&source=api"
            ).json()
            print(f"overridden response: {overridden_response}")
    finally:
        app.dependency_overrides.clear()
