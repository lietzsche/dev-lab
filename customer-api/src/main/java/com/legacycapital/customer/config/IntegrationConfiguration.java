package com.legacycapital.customer.config;

import com.legacycapital.integration.CreditGateway;
import com.legacycapital.integration.HttpCreditGateway;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.client.RestTemplate;

@Configuration
public class IntegrationConfiguration {
    @Bean
    public RestTemplate restTemplate() { return new RestTemplate(); }

    @Bean
    public CreditGateway creditGateway(RestTemplate restTemplate,
                                       @Value("${legacy.credit.base-url}") String baseUrl) {
        return new HttpCreditGateway(restTemplate, baseUrl);
    }
}
