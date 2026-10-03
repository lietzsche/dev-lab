package com.legacycapital.customer.service;

public class CustomerNotFoundException extends RuntimeException {
    public CustomerNotFoundException(String customerNumber) {
        super("customer not found: " + customerNumber);
    }
}
