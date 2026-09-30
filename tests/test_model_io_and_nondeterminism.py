"""Public behavior tests for P12-1 model I/O boundaries."""

from random import Random

import pytest
from pydantic import ValidationError

from knowledge_lab.lessons.p12_1_model_io_and_nondeterminism import (
    Message,
    answer_question,
    build_messages,
    estimate_token_count,
    fits_context_window,
    generate_fake_answer,
    parse_structured_answer,
)


class RecordingModelClient:
    def __init__(self, output: str) -> None:
        self.output = output
        self.calls: list[tuple[list[Message], float]] = []

    def complete(self, messages: list[Message], temperature: float) -> str:
        self.calls.append((messages, temperature))
        return self.output


def test_messages_and_context_budget_are_deterministic() -> None:
    messages = build_messages("What is a Python iterator?")

    assert messages == [
        {"role": "system", "content": "Answer using the provided notes."},
        {"role": "user", "content": "What is a Python iterator?"},
    ]
    assert estimate_token_count(messages) == 10
    assert fits_context_window(messages, 16, 6)
    assert not fits_context_window(messages, 15, 6)


def test_seeded_fake_sampling_exposes_temperature_behavior() -> None:
    random_source = Random(7)

    cold_answers = {generate_fake_answer(0.0, random_source) for _ in range(5)}
    warm_answers = {generate_fake_answer(1.0, random_source) for _ in range(10)}

    assert len(cold_answers) == 1
    assert len(warm_answers) == 3
    with pytest.raises(ValueError, match="temperature must be non-negative"):
        generate_fake_answer(-0.1, random_source)


def test_structured_output_validates_json_shape() -> None:
    parsed = parse_structured_answer(
        '{"answer":"One item at a time.","citations":["Python iterator"]}'
    )

    assert parsed.model_dump() == {
        "answer": "One item at a time.",
        "citations": ["Python iterator"],
    }

    with pytest.raises(ValidationError) as captured:
        parse_structured_answer(
            '{"answer":"One item at a time.","citations":"Python iterator"}'
        )

    assert captured.value.errors()[0]["loc"] == ("citations",)
    assert captured.value.errors()[0]["type"] == "list_type"


def test_application_uses_model_contract_and_validates_response() -> None:
    client = RecordingModelClient(
        '{"answer":"One item at a time.","citations":["Python iterator"]}'
    )

    result = answer_question("What is a Python iterator?", client, temperature=0.25)

    assert result.model_dump() == {
        "answer": "One item at a time.",
        "citations": ["Python iterator"],
    }
    assert client.calls == [
        (
            build_messages("What is a Python iterator?"),
            0.25,
        )
    ]
