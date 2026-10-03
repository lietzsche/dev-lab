package com.legacycapital.integration;

import com.legacycapital.common.CustomerNumber;
import org.springframework.web.client.RestTemplate;

public class HttpCreditGateway implements CreditGateway {
    private final RestTemplate restTemplate;
    private final String baseUrl;

    public HttpCreditGateway(RestTemplate restTemplate, String baseUrl) {
        this.restTemplate = restTemplate;
        this.baseUrl = baseUrl;
    }

    @Override
    public CreditGrade inquire(CustomerNumber customerNumber) {
        return restTemplate.getForObject(baseUrl + "/credit/{customerNumber}", CreditGrade.class,
                customerNumber.getValue());
    }
}
