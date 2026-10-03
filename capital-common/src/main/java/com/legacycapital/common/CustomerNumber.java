package com.legacycapital.common;

import java.io.Serializable;
import java.util.Objects;

public final class CustomerNumber implements Serializable {
    private static final long serialVersionUID = 1L;
    private final String value;

    public CustomerNumber(String value) {
        if (value == null || !value.matches("CUST-[0-9]{4}")) {
            throw new IllegalArgumentException("invalid customer number: " + value);
        }
        this.value = value;
    }

    public String getValue() { return value; }

    @Override public boolean equals(Object other) {
        return this == other || other instanceof CustomerNumber && value.equals(((CustomerNumber) other).value);
    }

    @Override public int hashCode() { return Objects.hash(value); }
    @Override public String toString() { return value; }
}
