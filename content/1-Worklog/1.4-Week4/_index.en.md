---
title: "Worklog Week 4"
date: 2026-04-19
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

**Duration:** May 11, 2026 – May 17, 2026

## Week 4 objectives

- Design the overall system architecture.
- Design the data flow and alerting mechanism.
- Prepare the AWS environment and configure IAM Roles.

## Work completed

- Designed the overall system architecture including a Training Zone and a Real-time Inference Zone.
- Designed the data flow from API Gateway → Lambda → Kinesis → SageMaker Endpoint → Firehose → Amazon S3.
- Designed the alerting mechanism via Amazon SNS when fraudulent transactions are detected.
- Prepared the AWS environment and configured IAM Roles for the services.

## Results achieved

- Completed the overall architecture design with two zones: Training and Real-time Inference.
- Clearly defined the end-to-end data flow from API Gateway to Amazon S3.
- Completed the alerting mechanism design via Amazon SNS.
- AWS environment and IAM Roles configured, ready for deployment.
