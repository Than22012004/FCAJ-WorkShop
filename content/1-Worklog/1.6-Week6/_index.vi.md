---
title: "Worklog Tuần 6"
date: 2026-04-19
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

**Thời gian:** 25/05 – 31/05

## Mục tiêu tuần 6

- Đóng gói mô hình và viết file inference.py.
- Upload mô hình lên Amazon S3.
- Triển khai SageMaker Real-time Endpoint và kiểm thử.

## Công việc đã thực hiện

- Đóng gói mô hình thành file model.tar.gz.
- Viết file inference.py phục vụ suy luận thời gian thực.
- Upload mô hình lên Amazon S3.
- Triển khai mô hình dưới dạng Amazon SageMaker Real-time Endpoint.
- Kiểm thử Endpoint bằng dữ liệu mẫu và đánh giá thời gian phản hồi.

## Kết quả đạt được

- Đóng gói mô hình thành công dưới dạng model.tar.gz.
- Hoàn thành inference.py với đầy đủ hàm model_fn, input_fn, predict_fn, output_fn.
- Upload mô hình lên Amazon S3 và triển khai SageMaker Endpoint thành công.
- Endpoint hoạt động ổn định với thời gian phản hồi đạt yêu cầu cho realtime.
