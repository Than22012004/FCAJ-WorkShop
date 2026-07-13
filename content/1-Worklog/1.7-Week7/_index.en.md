---
title: "Worklog Week 7"
date: 2026-04-19
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

**Duration:** June 01, 2026 – June 07, 2026

## Week 7 objectives

- Build a REST API using Amazon API Gateway.
- Develop an AWS Lambda to receive data.
- Normalize input data and send it to Amazon Kinesis Data Streams.

## Work completed

- Built a REST API using Amazon API Gateway to receive transactions.
- Developed an AWS Lambda to receive data from API Gateway.
- Normalized input data and sent it to Amazon Kinesis Data Streams.
- Tested data transmission from Client to Kinesis.

## Results achieved

- API operated stably, accepting transaction data via POST method.
- Lambda received events from API Gateway and normalized data successfully.
- Transaction data was transmitted from the Client to Kinesis Data Streams.
- Ready for the next step: stream-processing Lambda to call SageMaker.
