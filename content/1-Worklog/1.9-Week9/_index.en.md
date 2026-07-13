---
title: "Worklog Week 9"
date: 2026-04-19
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---

**Duration:** June 15, 2026 – June 21, 2026

## Week 9 objectives

- Integrate the SageMaker Endpoint with the real-time data processing pipeline.
- Classify legitimate and fraudulent transactions.
- Test and evaluate system stability.

## Work completed

- Integrated the SageMaker Endpoint with the real-time data processing pipeline.
- Classified legitimate and fraudulent transactions.
- Tested continuous prediction capability with simulated data.
- Evaluated system stability and processing time per transaction.

## Results achieved

- SageMaker Endpoint successfully integrated with the real-time data processing pipeline.
- System accurately classified legitimate transactions (prediction = 0) and fraudulent ones (prediction = 1).
- Continuous prediction testing with simulated data yielded stable results.
- Pipeline Kinesis → Lambda → SageMaker complete, ready for SNS and Firehose integration.
