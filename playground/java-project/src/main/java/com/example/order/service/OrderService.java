package com.example.order.service;

import com.example.order.domain.Order;
import com.example.order.domain.OrderStatus;
import com.example.order.repository.OrderRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import java.util.List;

@Service
public class OrderService {

    private final OrderRepository orderRepository;
    private final PaymentGatewayService paymentGatewayService;

    public OrderService(OrderRepository orderRepository, PaymentGatewayService paymentGatewayService) {
        this.orderRepository = orderRepository;
        this.paymentGatewayService = paymentGatewayService;
    }

    @Transactional(readOnly = true)
    public List<Order> findOrdersByStatus(String status) {
        return orderRepository.findByStatus(status);
    }

    @Transactional(readOnly = true)
    public Order getOrderOrThrow(String orderId) {
        Order order = orderRepository.findById(orderId);
        if (order == null) {
            throw new IllegalArgumentException("ERR_ORDER_NOT_FOUND: orderId=" + orderId);
        }
        return order;
    }

    @Transactional
    public Order placeOrder(Order order) {
        // FIXME: 재고 차감 중 데드락(ERR_DB_LOCK) 발생 시 재시도 로직 추가 필요
        if (order.getAmount() <= 0) {
            throw new IllegalArgumentException("ERR_INVALID_AMOUNT: amount must be positive");
        }
        paymentGatewayService.requestApproval(order.getOrderId(), order.getAmount());
        order.setStatus(OrderStatus.APPROVED);
        return orderRepository.save(order);
    }
}
