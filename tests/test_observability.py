"""Public behavior tests for P10-3 observability boundaries."""

import json
import time
import unittest

from knowledge_lab.lessons.p10_3_observability import (
    MetricsCollector,
    bind_request_id,
    handle_note_request,
    setup_json_logger,
    setup_memory_logger,
)


class ObservabilityTest(unittest.TestCase):
    def test_setup_memory_logger_filters_by_level(self) -> None:
        logger, buffer = setup_memory_logger("test.filter")

        logger.debug("hidden debug")
        logger.info("visible info")
        logger.warning("visible warning")

        lines = buffer.getvalue().splitlines()
        self.assertEqual(2, len(lines))
        self.assertEqual("INFO:test.filter:visible info", lines[0])
        self.assertEqual("WARNING:test.filter:visible warning", lines[1])

    def test_json_formatter_serializes_structured_fields(self) -> None:
        logger, buffer = setup_json_logger("test.json")

        logger.info("노트 저장 완료", extra={"event": "note_saved", "note_id": 100})

        data = json.loads(buffer.getvalue().strip())
        self.assertEqual("INFO", data["level"])
        self.assertEqual("노트 저장 완료", data["message"])
        self.assertEqual("test.json", data["name"])
        self.assertEqual("note_saved", data["event"])
        self.assertEqual(100, data["note_id"])

    def test_bind_request_id_injects_and_resets_context(self) -> None:
        logger, buffer = setup_json_logger("test.request_id")

        with bind_request_id("req-ctx-001"):
            logger.info("요청 처리 중")

        logger.info("요청 외부 작업")

        lines = [json.loads(line) for line in buffer.getvalue().splitlines()]
        self.assertEqual(2, len(lines))
        self.assertEqual("req-ctx-001", lines[0].get("request_id"))
        self.assertNotIn("request_id", lines[1])

    def test_metrics_collector_tracks_operations_and_errors(self) -> None:
        collector = MetricsCollector()

        with collector.track():
            time.sleep(0.002)

        self.assertEqual(1, collector.request_count)
        self.assertEqual(0, collector.error_count)
        self.assertGreater(collector.last_duration_ms, 0)
        self.assertEqual(collector.total_duration_ms, collector.last_duration_ms)

        with self.assertRaises(ValueError):
            with collector.track():
                raise ValueError("강제 예외 발생")

        self.assertEqual(2, collector.request_count)
        self.assertEqual(1, collector.error_count)
        self.assertGreater(collector.total_duration_ms, collector.last_duration_ms)

    def test_handle_note_request_separates_public_error_from_internal_trace(
        self,
    ) -> None:
        logger, buffer = setup_json_logger("test.error_boundary")

        response = handle_note_request(-10, logger)

        # 1. 사용자에게 전달되는 공개 응답: 내부 스택트레이스 없음
        self.assertEqual("요청을 처리할 수 없습니다", response.get("error"))
        self.assertEqual("INVALID_NOTE", response.get("code"))
        self.assertNotIn("Traceback", json.dumps(response))

        # 2. 내부 로그: 스택트레이스 및 비즈니스 메타데이터 보존
        log_entry = json.loads(buffer.getvalue().strip())
        self.assertEqual("ERROR", log_entry["level"])
        self.assertEqual("note_error", log_entry["event"])
        self.assertEqual(-10, log_entry["note_id"])
        self.assertIn("Traceback (most recent call last):", log_entry["exception"])
        self.assertIn("ValueError: 유효하지 않은 노트 ID: -10", log_entry["exception"])


if __name__ == "__main__":
    unittest.main()
