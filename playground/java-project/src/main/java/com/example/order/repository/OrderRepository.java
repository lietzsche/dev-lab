package com.example.order.repository;

import com.example.order.domain.Order;
import org.springframework.stereotype.Repository;
import java.util.Collections;
import java.util.List;

@Repository
public class OrderRepository {

    public Order findById(String orderId) {
        return null;
    }

    public List<Order> findByStatus(String status) {
        return Collections.emptyList();
    }

    public Order save(Order order) {
        return order;
    }
}
