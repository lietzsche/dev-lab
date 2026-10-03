package com.legacycapital.customer.domain;

import com.legacycapital.common.ContractStatus;
import java.math.BigDecimal;
import javax.persistence.Entity;
import javax.persistence.EnumType;
import javax.persistence.Enumerated;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "capital_contracts")
public class CapitalContract {
    @Id private Long id;
    private String customerNumber;
    private BigDecimal principal;
    @Enumerated(EnumType.STRING) private ContractStatus status;

    protected CapitalContract() { }

    public CapitalContract(Long id, String customerNumber, BigDecimal principal, ContractStatus status) {
        this.id = id;
        this.customerNumber = customerNumber;
        this.principal = principal;
        this.status = status;
    }

    public Long getId() { return id; }
    public String getCustomerNumber() { return customerNumber; }
    public BigDecimal getPrincipal() { return principal; }
    public ContractStatus getStatus() { return status; }
}
