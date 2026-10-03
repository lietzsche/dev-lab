package com.legacycapital.customer.web;

import com.legacycapital.customer.service.CustomerInquiryService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/customers")
public class CustomerController {
    private final CustomerInquiryService service;

    public CustomerController(CustomerInquiryService service) { this.service = service; }

    @GetMapping("/{customerNumber}")
    public CustomerResponse find(@PathVariable String customerNumber) {
        return new CustomerResponse(service.find(customerNumber));
    }
}
