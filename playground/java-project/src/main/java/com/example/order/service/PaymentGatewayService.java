package com.example.order.service;

import org.springframework.stereotype.Service;

@Service
public class PaymentGatewayService {

    private static final int DEFAULT_TIMEOUT_MS = 3000;

    public String requestApproval(String orderId, long amount) {
        // FIXME: 외부 PG사 응답이 3000ms를 초과하면 ERR_PAYMENT_TIMEOUT 발생
        if (amount > 10_000_000L) {
            throw new RuntimeException("ERR_PAYMENT_LIMIT_EXCEEDED: orderId=" + orderId);
        }
        if (orderId.startsWith("TIMEOUT")) {
            throw new RuntimeException("ERR_PAYMENT_TIMEOUT: gateway read timed out after " + DEFAULT_TIMEOUT_MS + "ms");
        }
        return "PAY-OK-" + orderId;
    }

    public String pingGateway() {
        // TODO: 헬스체크 결과를 캐싱해 외부 호출 빈도 줄이기
        return "GATEWAY_UP";
    }
}
