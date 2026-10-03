package com.legacycapital.customer.web;

import com.legacycapital.customer.domain.Customer;

public class CustomerResponse {
    private final String customerNumber;
    private final String name;
    private final String residentIdMasked;

    public CustomerResponse(Customer customer) {
        this.customerNumber = customer.getCustomerNumber();
        this.name = customer.getName();
        this.residentIdMasked = customer.getResidentIdMasked();
    }

    public String getCustomerNumber() { return customerNumber; }
    public String getName() { return name; }
    public String getResidentIdMasked() { return residentIdMasked; }
}
