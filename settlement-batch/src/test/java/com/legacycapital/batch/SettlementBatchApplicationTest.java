package com.legacycapital.batch;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.batch.core.BatchStatus;
import org.springframework.batch.core.Job;
import org.springframework.batch.core.JobExecution;
import org.springframework.batch.test.JobLauncherTestUtils;
import org.springframework.batch.test.context.SpringBatchTest;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import static org.junit.Assert.assertEquals;

@SpringBatchTest
@RunWith(SpringRunner.class)
@SpringBootTest
public class SettlementBatchApplicationTest {
    @Autowired private JobLauncherTestUtils jobLauncherTestUtils;
    @Autowired private Job dailySettlement;

    @Test public void completesDailySettlement() throws Exception {
        jobLauncherTestUtils.setJob(dailySettlement);
        JobExecution execution = jobLauncherTestUtils.launchJob();
        assertEquals(BatchStatus.COMPLETED, execution.getStatus());
    }
}
