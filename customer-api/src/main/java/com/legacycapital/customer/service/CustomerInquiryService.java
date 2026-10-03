package com.legacycapital.customer.service;

import com.legacycapital.customer.domain.Customer;
import com.legacycapital.customer.repository.CustomerRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class CustomerInquiryService {
    private final CustomerRepository repository;

    public CustomerInquiryService(CustomerRepository repository) { this.repository = repository; }

    @Transactional(readOnly = true)
    public Customer find(String customerNumber) {
        return repository.findById(customerNumber)
                .orElseThrow(() -> new CustomerNotFoundException(customerNumber));
    }
}
