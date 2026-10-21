#!/usr/bin/env python3
"""Level 4 & Level 7 실습용 로컬 HTTP 모의 서버 (기본 포트: 18080)"""
import json
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer


class MockOrderHandler(BaseHTTPRequestHandler):
    def _send_json(self, status_code: int, payload: dict) -> None:
        body = (json.dumps(payload, ensure_ascii=False) + "\n").encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if self.path == "/health":
            self._send_json(200, {"status": "UP", "service": "order-service"})
        elif self.path == "/api/orders":
            self._send_json(
                200,
                {
                    "orders": [
                        {"orderId": "ORD-2001", "status": "APPROVED", "amount": 35000},
                        {"orderId": "ORD-2002", "status": "APPROVED", "amount": 52000},
                    ]
                },
            )
        else:
            self._send_json(404, {"error": "NOT_FOUND", "path": self.path})

    def do_POST(self) -> None:
        if self.path == "/api/orders":
            length = int(self.headers.get("Content-Length", "0"))
            raw = self.rfile.read(length).decode("utf-8") if length > 0 else "{}"
            self._send_json(
                201,
                {"result": "CREATED", "orderId": "ORD-3001", "received": raw},
            )
        else:
            self._send_json(404, {"error": "NOT_FOUND", "path": self.path})

    def log_message(self, fmt: str, *args) -> None:
        sys.stderr.write(f"[mock-server] {self.address_string()} - {fmt % args}\n")


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 18080
    server = HTTPServer(("127.0.0.1", port), MockOrderHandler)
    print(f"[mock-server] Listening on http://127.0.0.1:{port} (PID={__import__('os').getpid()})")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[mock-server] Shutting down.")
        server.server_close()
