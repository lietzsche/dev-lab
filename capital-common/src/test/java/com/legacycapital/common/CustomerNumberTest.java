package com.legacycapital.common;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class CustomerNumberTest {
    @Test public void acceptsLegacyCustomerNumber() {
        assertEquals("CUST-1001", new CustomerNumber("CUST-1001").getValue());
    }
}
