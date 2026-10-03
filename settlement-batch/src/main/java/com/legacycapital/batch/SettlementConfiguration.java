package com.legacycapital.batch;

import com.legacycapital.common.LegacyDigest;
import java.math.BigDecimal;
import java.util.Arrays;
import org.springframework.batch.core.Job;
import org.springframework.batch.core.Step;
import org.springframework.batch.core.configuration.annotation.JobBuilderFactory;
import org.springframework.batch.core.configuration.annotation.StepBuilderFactory;
import org.springframework.batch.item.ItemProcessor;
import org.springframework.batch.item.support.ListItemReader;
import org.springframework.batch.item.support.ListItemWriter;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class SettlementConfiguration {
    @Bean
    public Job dailySettlement(JobBuilderFactory jobs, Step settlementStep) {
        return jobs.get("dailySettlement").start(settlementStep).build();
    }

    @Bean
    public Step settlementStep(StepBuilderFactory steps) {
        return steps.get("settlementStep")
                .<SettlementItem, SettlementItem>chunk(10)
                .reader(new ListItemReader<>(Arrays.asList(
                        new SettlementItem("CNTR-10001", new BigDecimal("30000000")),
                        new SettlementItem("CNTR-10002", new BigDecimal("12500000")))))
                .processor((ItemProcessor<SettlementItem, SettlementItem>) item -> {
                    item.setChecksum(LegacyDigest.sha256(item.getContractNumber()));
                    return item;
                })
                .writer(new ListItemWriter<>())
                .build();
    }
}
