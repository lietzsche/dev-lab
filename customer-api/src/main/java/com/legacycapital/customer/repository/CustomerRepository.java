package com.legacycapital.customer.repository;

import com.legacycapital.customer.domain.Customer;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CustomerRepository extends JpaRepository<Customer, String> { }
