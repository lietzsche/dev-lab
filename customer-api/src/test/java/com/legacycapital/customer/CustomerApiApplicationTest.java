package com.legacycapital.customer;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.test.context.junit4.SpringRunner;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

@RunWith(SpringRunner.class)
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
public class CustomerApiApplicationTest {
    @Autowired private TestRestTemplate restTemplate;

    @Test public void returnsExistingCustomer() {
        ResponseEntity<String> response = restTemplate.getForEntity("/api/customers/CUST-1001", String.class);
        assertEquals(HttpStatus.OK, response.getStatusCode());
        assertTrue(response.getBody().contains("Kim Legacy"));
    }

    @Test public void returnsNotFoundForUnknownCustomer() {
        ResponseEntity<String> response = restTemplate.getForEntity("/api/customers/CUST-9999", String.class);
        assertEquals(HttpStatus.NOT_FOUND, response.getStatusCode());
    }
}
