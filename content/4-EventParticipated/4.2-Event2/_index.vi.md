---
title: "Sự kiện 2 - Các giải pháp bảo mật và chứng chỉ AWS"
date: 2026-06-15
weight: 2
chapter: false
pre: " <b> 4.2. </b> "
---

## 1. Thông tin sự kiện

- **Tên sự kiện:** AWS Security & Certification Workshop
- **Thời gian:** Thứ Bảy, ngày 15 tháng 6
- **Địa điểm:** Văn phòng AWS Việt Nam
- **Vai trò tham gia:** Khách mời

## 2. Hình ảnh minh chứng

![Minh chứng tham gia Sự kiện 2](https://than22012004.github.io/FCAJ-WorkShop/images/event_2.jpg)

## 3. Nội dung chương trình

Sự kiện tập trung vào các chủ đề quan trọng khi vận hành hệ thống thực tế trên nền tảng đám mây, bao gồm bảo mật, cam kết chất lượng dịch vụ và định hướng nghề nghiệp thông qua các chứng chỉ của AWS.

### 09:00 - 10:00: AWS Security Agent

Phiên mở đầu giới thiệu về **AWS Security Agent** và các phương pháp tiếp cận bảo mật toàn diện trên đám mây. Diễn giả trình bày cách các tác tử bảo mật có thể tự động giám sát, phát hiện các mối đe dọa tiềm ẩn và phản ứng theo thời gian thực. Nội dung cũng đi sâu vào cách thiết lập các Guardrails, nguyên tắc đặc quyền tối thiểu (Least Privilege) và việc tích hợp các quy trình bảo mật (DevSecOps) vào vòng đời phát triển phần mềm mà không làm chậm tốc độ triển khai.

### 10:00 - 10:45: Giới thiệu về SLA (Service Level Agreement)

Phiên thứ hai tập trung vào khái niệm **SLA (Service Level Agreement)** - Cam kết chất lượng dịch vụ. Người tham gia được tìm hiểu cách đọc, phân tích các tài liệu SLA của AWS cho từng dịch vụ cụ thể (như Amazon S3, EC2, API Gateway). Diễn giả giải thích các khái niệm như Uptime (Thời gian hoạt động), RTO (Recovery Time Objective), RPO (Recovery Point Objective) và cách kiến trúc hệ thống để đáp ứng được các mức SLA cao (như 99.99% hoặc 99.999%) thông qua Multi-AZ và Multi-Region.

### 10:45 - 11:00: Nghỉ giải lao

Giao lưu, networking và thảo luận với các chuyên gia bảo mật.

### 11:00 - 12:00: Hướng dẫn cách ôn thi các chứng chỉ của AWS

Phiên cuối cùng rất thiết thực đối với những người mới bắt đầu và đang định hướng nghề nghiệp trên Cloud. Diễn giả chia sẻ lộ trình lấy các chứng chỉ của AWS (từ Cloud Practitioner, Associate, Professional đến Specialty). Nội dung bao gồm cách đăng ký thi, các nguồn tài liệu học tập chính thức và miễn phí (như AWS Skill Builder), chiến thuật làm bài thi, và cách lấy kinh nghiệm thực hành (hands-on) thông qua việc tự xây dựng các dự án (như Data Lake hoặc Fraud Detection).

## 4. Kết quả đạt được và bài học kinh nghiệm

Tham gia sự kiện thứ 2 mang lại cho tôi cái nhìn tổng quan và thực tế hơn về việc thiết kế một hệ thống không chỉ hoạt động được mà còn phải bảo mật và có độ sẵn sàng cao.

Kiến thức về **AWS Security Agent** giúp tôi hiểu rõ tầm quan trọng của việc bảo mật hệ thống. Trong dự án phát hiện gian lận của mình, việc quản lý quyền truy cập bằng IAM Role cho các dịch vụ (Lambda, API Gateway, SageMaker) cần được thiết lập cẩn thận theo nguyên tắc đặc quyền tối thiểu, đồng thời việc theo dõi logs từ CloudWatch cũng đóng vai trò giống như một lớp giám sát bảo mật.

Phần giới thiệu về **SLA** giúp tôi nâng cao tư duy kiến trúc. Khi thiết kế pipeline thời gian thực với Kinesis và SageMaker, tôi phải bắt đầu cân nhắc việc các dịch vụ này cam kết Uptime như thế nào, và hệ thống của tôi sẽ xử lý ra sao nếu một thành phần tạm thời không phản hồi.

Cuối cùng, phần chia sẻ về **chứng chỉ AWS** đã tiếp thêm động lực và định hướng lộ trình học tập rõ ràng. Nó chứng minh rằng những dự án thực tế như hệ thống Real-time ML on AWS mà tôi đang xây dựng là bước đệm tốt nhất để hiểu sâu về dịch vụ, hỗ trợ rất nhiều cho việc đạt được các chứng chỉ uy tín của AWS trong tương lai.
