---
title: "Worklog Tuần 4"
date: 2026-04-19
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

**Thời gian:** 11/05 – 17/05

## Mục tiêu tuần 4

- Thiết kế kiến trúc tổng thể của hệ thống.
- Thiết kế luồng dữ liệu và cơ chế cảnh báo.
- Chuẩn bị môi trường AWS và cấu hình IAM Role.

## Công việc đã thực hiện

- Thiết kế kiến trúc tổng thể của hệ thống gồm Training Zone và Real-time Inference Zone.
- Thiết kế luồng dữ liệu từ API Gateway → Lambda → Kinesis → SageMaker Endpoint → Firehose → Amazon S3.
- Thiết kế cơ chế gửi cảnh báo thông qua Amazon SNS khi phát hiện giao dịch gian lận.
- Chuẩn bị môi trường AWS và cấu hình IAM Role cho các dịch vụ.

## Kết quả đạt được

- Hoàn thành thiết kế kiến trúc tổng thể với hai zone: Training và Real-time Inference.
- Xác định rõ luồng dữ liệu end-to-end từ API Gateway đến Amazon S3.
- Thiết kế xong cơ chế gửi cảnh báo qua Amazon SNS.
- Môi trường AWS và IAM Role đã được cấu hình, sẵn sàng triển khai.
