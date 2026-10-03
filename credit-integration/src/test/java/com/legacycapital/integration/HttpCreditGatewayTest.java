package com.legacycapital.integration;

import com.legacycapital.common.CustomerNumber;
import org.junit.Test;
import org.springframework.http.MediaType;
import org.springframework.test.web.client.MockRestServiceServer;
import org.springframework.web.client.RestTemplate;

import static org.junit.Assert.assertEquals;
import static org.springframework.test.web.client.match.MockRestRequestMatchers.requestTo;
import static org.springframework.test.web.client.response.MockRestResponseCreators.withSuccess;

public class HttpCreditGatewayTest {
    @Test public void readsCreditGradeFromLegacyProvider() {
        RestTemplate template = new RestTemplate();
        MockRestServiceServer server = MockRestServiceServer.createServer(template);
        server.expect(requestTo("http://credit.local/credit/CUST-1001"))
                .andRespond(withSuccess("{\"customerNumber\":\"CUST-1001\",\"score\":760,\"grade\":\"A\"}", MediaType.APPLICATION_JSON));

        CreditGrade grade = new HttpCreditGateway(template, "http://credit.local")
                .inquire(new CustomerNumber("CUST-1001"));

        assertEquals("A", grade.getGrade());
        server.verify();
    }
}
