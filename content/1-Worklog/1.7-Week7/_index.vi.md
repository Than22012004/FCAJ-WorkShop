---
title: "Worklog Tuần 7"
date: 2026-04-19
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

**Thời gian:** 01/06 – 07/06

## Mục tiêu tuần 7

- Xây dựng REST API bằng Amazon API Gateway.
- Phát triển AWS Lambda tiếp nhận dữ liệu.
- Chuẩn hóa dữ liệu và gửi vào Amazon Kinesis Data Streams.

## Công việc đã thực hiện

- Xây dựng REST API bằng Amazon API Gateway để tiếp nhận giao dịch.
- Phát triển AWS Lambda tiếp nhận dữ liệu từ API Gateway.
- Chuẩn hóa dữ liệu đầu vào và gửi dữ liệu vào Amazon Kinesis Data Streams.
- Kiểm thử việc truyền dữ liệu từ Client đến Kinesis.

## Kết quả đạt được

- API hoạt động ổn định, tiếp nhận dữ liệu giao dịch qua POST method.
- Lambda nhận được event từ API Gateway, chuẩn hóa dữ liệu thành công.
- Dữ liệu giao dịch đã truyền được từ Client đến Kinesis Data Streams.
- Sẵn sàng cho bước tiếp theo: Lambda xử lý stream và gọi SageMaker.
