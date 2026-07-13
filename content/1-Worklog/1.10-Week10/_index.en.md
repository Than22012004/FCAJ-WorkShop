---
title: "Worklog Week 10"
date: 2026-04-19
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

**Duration:** June 22, 2026 – June 28, 2026

## Week 10 objectives

- Configure Amazon SNS to send alerts when fraudulent transactions are detected.
- Set up Amazon Kinesis Firehose to store transaction history.
- Test the complete data flow and system scalability.

## Work completed

- Configured Amazon SNS to send alert emails when fraudulent transactions are detected.
- Set up Amazon Kinesis Firehose to store all transaction history in Amazon S3.
- Tested the complete data flow from API Gateway to Amazon S3.
- Verified the storage mechanism and system scalability.

## Results achieved

- SNS successfully sent alert emails when fraudulent transactions were detected.
- Kinesis Firehose stored transaction history in S3 stably.
- End-to-end testing passed: API Gateway → Lambda → Kinesis → SageMaker → SNS/Firehose → S3.
- The basic real-time fraud detection system is functionally complete.
