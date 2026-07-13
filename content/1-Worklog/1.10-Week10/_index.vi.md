---
title: "Worklog Tuần 10"
date: 2026-04-19
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

**Thời gian:** 22/06 – 28/06

## Mục tiêu tuần 10

- Cấu hình Amazon SNS gửi cảnh báo khi phát hiện giao dịch gian lận.
- Thiết lập Amazon Kinesis Firehose lưu lịch sử giao dịch.
- Kiểm thử luồng dữ liệu hoàn chỉnh và khả năng mở rộng.

## Công việc đã thực hiện

- Cấu hình Amazon SNS gửi email cảnh báo khi phát hiện giao dịch gian lận.
- Thiết lập Amazon Kinesis Firehose lưu toàn bộ lịch sử giao dịch vào Amazon S3.
- Kiểm thử luồng dữ liệu hoàn chỉnh từ API Gateway đến Amazon S3.
- Kiểm tra cơ chế lưu trữ và khả năng mở rộng của hệ thống.

## Kết quả đạt được

- SNS gửi email cảnh báo thành công khi phát hiện giao dịch gian lận.
- Kinesis Firehose lưu lịch sử giao dịch vào S3 ổn định.
- Kiểm thử thành công luồng dữ liệu end-to-end: API Gateway → Lambda → Kinesis → SageMaker → SNS/Firehose → S3.
- Hệ thống realtime fraud detection cơ bản hoàn chỉnh.
