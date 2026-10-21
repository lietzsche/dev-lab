package com.example.order.controller;

import com.example.order.service.PaymentGatewayService;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/payments")
public class PaymentController {

    private final PaymentGatewayService paymentGatewayService;

    public PaymentController(PaymentGatewayService paymentGatewayService) {
        this.paymentGatewayService = paymentGatewayService;
    }

    @PostMapping("/approve")
    public String approvePayment(@RequestParam String orderId, @RequestParam long amount) {
        return paymentGatewayService.requestApproval(orderId, amount);
    }

    @GetMapping("/health")
    public String checkGatewayHealth() {
        return paymentGatewayService.pingGateway();
    }
}
