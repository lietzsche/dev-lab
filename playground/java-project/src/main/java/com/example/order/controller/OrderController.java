package com.example.order.controller;

import com.example.order.domain.Order;
import com.example.order.service.OrderService;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/orders")
public class OrderController {

    private final OrderService orderService;

    public OrderController(OrderService orderService) {
        this.orderService = orderService;
    }

    @GetMapping
    public List<Order> listOrders(@RequestParam(defaultValue = "ALL") String status) {
        return orderService.findOrdersByStatus(status);
    }

    @GetMapping("/{orderId}")
    public Order getOrder(@PathVariable String orderId) {
        return orderService.getOrderOrThrow(orderId);
    }

    @PostMapping
    public Order createOrder(@RequestBody Order request) {
        // TODO: 요청 DTO 검증 어노테이션(@Valid) 추가 필요
        return orderService.placeOrder(request);
    }
}
