package com.legacycapital.batch;

import java.math.BigDecimal;

public class SettlementItem {
    private final String contractNumber;
    private final BigDecimal principal;
    private String checksum;

    public SettlementItem(String contractNumber, BigDecimal principal) {
        this.contractNumber = contractNumber;
        this.principal = principal;
    }

    public String getContractNumber() { return contractNumber; }
    public BigDecimal getPrincipal() { return principal; }
    public String getChecksum() { return checksum; }
    public void setChecksum(String checksum) { this.checksum = checksum; }
}
