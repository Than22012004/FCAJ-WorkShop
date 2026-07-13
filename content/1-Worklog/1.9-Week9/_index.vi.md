---
title: "Worklog Tuần 9"
date: 2026-04-19
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---

**Thời gian:** 15/06 – 21/06

## Mục tiêu tuần 9

- Tích hợp SageMaker Endpoint với pipeline xử lý dữ liệu thời gian thực.
- Phân loại giao dịch hợp lệ và giao dịch gian lận.
- Kiểm thử và đánh giá độ ổn định của hệ thống.

## Công việc đã thực hiện

- Tích hợp SageMaker Endpoint với pipeline xử lý dữ liệu thời gian thực.
- Phân loại giao dịch hợp lệ và giao dịch gian lận.
- Kiểm thử khả năng dự đoán liên tục với dữ liệu mô phỏng.
- Đánh giá độ ổn định của hệ thống và thời gian xử lý từng giao dịch.

## Kết quả đạt được

- SageMaker Endpoint tích hợp thành công với pipeline xử lý dữ liệu thời gian thực.
- Hệ thống phân loại chính xác giao dịch hợp lệ (prediction = 0) và gian lận (prediction = 1).
- Kiểm thử dự đoán liên tục với dữ liệu mô phỏng cho kết quả ổn định.
- Pipeline Kinesis → Lambda → SageMaker hoàn chỉnh, sẵn sàng tích hợp SNS và Firehose.
