package com.example.order.domain;

public class Order {
    private String orderId;
    private String customerId;
    private long amount;
    private OrderStatus status;

    public Order(String orderId, String customerId, long amount, OrderStatus status) {
        this.orderId = orderId;
        this.customerId = customerId;
        this.amount = amount;
        this.status = status;
    }

    public String getOrderId() { return orderId; }
    public String getCustomerId() { return customerId; }
    public long getAmount() { return amount; }
    public OrderStatus getStatus() { return status; }
    public void setStatus(OrderStatus status) { this.status = status; }
}
