package com.legacycapital.customer.repository;

import com.legacycapital.customer.domain.CapitalContract;
import java.util.List;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ContractRepository extends JpaRepository<CapitalContract, Long> {
    List<CapitalContract> findByCustomerNumberOrderById(String customerNumber);
}
