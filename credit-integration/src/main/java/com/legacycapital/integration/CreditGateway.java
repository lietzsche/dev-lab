package com.legacycapital.integration;

import com.legacycapital.common.CustomerNumber;

public interface CreditGateway {
    CreditGrade inquire(CustomerNumber customerNumber);
}
