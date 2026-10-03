package com.legacycapital.customer.domain;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "customers")
public class Customer {
    @Id
    private String customerNumber;
    @Column(nullable = false)
    private String name;
    @Column(nullable = false)
    private String residentIdMasked;

    protected Customer() { }

    public Customer(String customerNumber, String name, String residentIdMasked) {
        this.customerNumber = customerNumber;
        this.name = name;
        this.residentIdMasked = residentIdMasked;
    }

    public String getCustomerNumber() { return customerNumber; }
    public String getName() { return name; }
    public String getResidentIdMasked() { return residentIdMasked; }
}
