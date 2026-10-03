package com.legacycapital.integration;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

public final class CreditGrade {
    private final String customerNumber;
    private final int score;
    private final String grade;

    @JsonCreator
    public CreditGrade(@JsonProperty("customerNumber") String customerNumber,
                       @JsonProperty("score") int score,
                       @JsonProperty("grade") String grade) {
        this.customerNumber = customerNumber;
        this.score = score;
        this.grade = grade;
    }

    public String getCustomerNumber() { return customerNumber; }
    public int getScore() { return score; }
    public String getGrade() { return grade; }
}
