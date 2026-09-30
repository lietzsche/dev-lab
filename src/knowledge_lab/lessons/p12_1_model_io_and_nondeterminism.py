"""P12-1: model I/O와 비결정성 경계를 관찰한다."""

from random import Random
from typing import Literal, Protocol, TypedDict

from pydantic import BaseModel, ValidationError


class Message(TypedDict):
    role: Literal["system", "user", "assistant"]
    content: str


class AnswerPayload(BaseModel):
    answer: str
    citations: list[str]


class ModelClient(Protocol):
    def complete(
        self,
        messages: list[Message],
        temperature: float,
    ) -> str: ...


class FakeModelClient:
    def complete(self, messages: list[Message], temperature: float) -> str:
        return (
            '{"answer": "An iterator returns one item at a time.", '
            '"citations": ["Python iterator"]}'
        )


def build_messages(question: str) -> list[Message]:
    return [
        Message(role="system", content="Answer using the provided notes."),
        Message(role="user", content=question),
    ]


def estimate_token_count(messages: list[Message]) -> int:
    token_count: int = 0
    for message in messages:
        token_count += len(message["content"].split())
    return token_count


def fits_context_window(
    messages: list[Message],
    context_window: int,
    reserved_output_tokens: int,
) -> bool:
    return estimate_token_count(messages) + reserved_output_tokens <= context_window


def generate_fake_answer(temperature: float, random_source: Random) -> str:
    answers = [
        "An iterator returns one item at a time.",
        "Iterators produce values lazily.",
        "Use next() to advance an iterator.",
    ]
    if temperature < 0:
        raise ValueError("temperature must be non-negative")
    if temperature == 0:
        return answers[0]
    return random_source.choice(answers)


def parse_structured_answer(raw_output: str) -> AnswerPayload:
    return AnswerPayload.model_validate_json(raw_output)


def answer_question(
    question: str,
    model_client: ModelClient,
    temperature: float = 0.0,
) -> AnswerPayload:
    messages = build_messages(question)
    raw_output = model_client.complete(messages, temperature)
    return parse_structured_answer(raw_output)


def run() -> None:
    """Run the current model I/O and nondeterminism exercise."""
    print()
    print("P12-1 model I/O와 비결정성 시작")

    question = "What is a Python iterator?"
    messages = build_messages(question)
    print(f"messages repr: {messages!r}")
    print(f"messages type: {type(messages)}")
    print(f"first message type: {type(messages[0])}")
    for message in messages:
        print(f"message role: {message['role']}")
        print(f"message content: {message['content']}")

    content_character_count: int = 0
    for message in messages:
        content_character_count += len(message["content"])
    estimated_token_count = estimate_token_count(messages)
    print(f"content character count: {content_character_count}")
    print(f"estimated token count: {estimated_token_count}")

    print(f"fits exact context: {fits_context_window(messages, 16, 6)}")
    print(f"fits small context: {fits_context_window(messages, 15, 6)}")

    cold_answers: set[str] = set()
    warm_answers: set[str] = set()
    random_source = Random(7)
    for _ in range(5):
        cold_answers.add(generate_fake_answer(0.0, random_source))
    for _ in range(10):
        warm_answers.add(generate_fake_answer(1.0, random_source))
    print(f"cold unique count: {len(cold_answers)}")
    print(f"warm unique count: {len(warm_answers)}")

    raw_output = (
        '{"answer": "An iterator returns one item at a time.",'
        '"citations": ["Python iterator"]}'
    )
    parsed_answer = parse_structured_answer(raw_output)
    print(f"raw output type: {type(raw_output)}")
    print(f"parsed answer repr: {parsed_answer!r}")
    print(f"parsed answer type: {type(parsed_answer)}")
    print(f"answer: {parsed_answer.answer}")
    print(f"citations: {parsed_answer.citations}")

    invalid_output = (
        '{"answer": "An iterator returns one item at a time.",'
        '"citations":"Python iterator"}'
    )
    try:
        parse_structured_answer(invalid_output)
    except ValidationError as error:
        first_error = error.errors()[0]
        print(f"error loc: {first_error['loc']}")
        print(f"error type: {first_error['type']}")
        print(f"error msg: {first_error['msg']}")
        print(f"error input: {first_error['input']}")

    client: ModelClient = FakeModelClient()
    application_result = answer_question(question, client, 0.0)
    print(f"client type: {type(client)}")
    print(f"application result: {application_result}")
    print(f"application result type: {type(application_result)}")
