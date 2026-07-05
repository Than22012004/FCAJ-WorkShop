---
title: "Tự đánh giá"
date: 2026-04-19
weight: 6
chapter: false
pre: " <b> 6. </b> "
---

Trong thời gian thực tập tại **AWS** với vị trí **Cloud Engineering**, tôi đã thực hiện project cá nhân **Xây dựng hệ thống phát hiện gian lận giao dịch thẻ tín dụng bằng Machine Learning trên nền tảng AWS**.

Mục tiêu của project là xây dựng một pipeline hoàn chỉnh từ quá trình huấn luyện mô hình đến triển khai dự đoán thời gian thực. Hệ thống được chia thành hai khu vực chính:

- **Training Zone**: lưu trữ dữ liệu trên Amazon S3, huấn luyện mô hình Random Forest bằng Amazon SageMaker, tạo model artifact và triển khai SageMaker Endpoint.
- **Real-time Zone**: tiếp nhận giao dịch thông qua API Gateway, xử lý bằng AWS Lambda, truyền dữ liệu qua Amazon Kinesis, thực hiện dự đoán bằng SageMaker Endpoint, gửi cảnh báo qua Amazon SNS và lưu kết quả vào Amazon S3 thông qua Kinesis Firehose.

Thông qua project, tôi không chỉ áp dụng kiến thức về Machine Learning mà còn có cơ hội tiếp cận quy trình xây dựng một hệ thống AI trên nền tảng Cloud theo hướng gần với thực tế triển khai doanh nghiệp.

Các nội dung chính đã thực hiện gồm:

- Phân tích bài toán phát hiện gian lận giao dịch thẻ tín dụng.
- Thiết kế kiến trúc hệ thống theo mô hình Training Zone và Real-time Zone.
- Xây dựng Data Lake trên Amazon S3 để lưu trữ dữ liệu huấn luyện, model artifact và kết quả dự đoán.
- Huấn luyện mô hình Random Forest bằng Amazon SageMaker và triển khai SageMaker Real-time Endpoint.
- Xây dựng pipeline xử lý giao dịch thời gian thực sử dụng API Gateway, Lambda, Amazon Kinesis và SageMaker Endpoint.
- Thiết lập cơ chế cảnh báo giao dịch gian lận bằng Amazon SNS.
- Lưu lịch sử giao dịch và kết quả dự đoán xuống Amazon S3 thông qua Kinesis Firehose.
- Viết tài liệu Workshop Website bằng Hugo, bao gồm Proposal, Worklog, Workshop, Blog, Events, Self Evaluation và Feedback.
- Thực hiện kiểm thử, ghi nhận kết quả và xây dựng quy trình dọn dẹp tài nguyên nhằm tối ưu chi phí sử dụng AWS.

Qua quá trình thực hiện, tôi tự đánh giá bản thân theo các tiêu chí sau:

| STT | Tiêu chí | Mức đánh giá | Nhận xét |
| --- | --- | --- | --- |
| 1 | **Kiến thức chuyên môn** | Tốt | Tôi đã vận dụng kiến thức về Machine Learning, Python và các dịch vụ AWS để xây dựng một hệ thống phát hiện gian lận hoàn chỉnh từ giai đoạn huấn luyện đến triển khai dự đoán thời gian thực. |
| 2 | **Khả năng học hỏi** | Tốt | Tôi chủ động nghiên cứu và sử dụng các dịch vụ như Amazon S3, SageMaker, API Gateway, Lambda, Kinesis, SNS và Firehose, đồng thời tìm hiểu cách các dịch vụ này phối hợp trong một hệ thống Machine Learning trên Cloud. |
| 3 | **Tính chủ động** | Tốt | Tôi chủ động thiết kế kiến trúc hệ thống, xây dựng pipeline xử lý dữ liệu và triển khai các thành phần thay vì chỉ thực hiện theo tài liệu hướng dẫn có sẵn. |
| 4 | **Tinh thần trách nhiệm** | Tốt | Tôi hoàn thành đầy đủ các nội dung của project, từ xây dựng hệ thống, kiểm thử, tối ưu tài nguyên đến hoàn thiện báo cáo và tài liệu hướng dẫn triển khai. |
| 5 | **Kỷ luật trong công việc** | Khá | Tôi luôn theo dõi tiến độ thực hiện và kiểm tra lại từng thành phần sau khi triển khai. Tuy nhiên, cần cải thiện khả năng quản lý thời gian để tối ưu quá trình hoàn thiện project. |
| 6 | **Khả năng giao tiếp và trình bày** | Tốt | Tôi trình bày nội dung báo cáo theo từng bước triển khai, kết hợp sơ đồ kiến trúc và hình ảnh minh họa giúp người đọc dễ theo dõi toàn bộ quy trình hoạt động của hệ thống. |
| 7 | **Khả năng làm việc nhóm / trao đổi** | Khá | Tôi tiếp thu các góp ý từ giảng viên và người hướng dẫn để điều chỉnh nội dung báo cáo cũng như cải thiện kiến trúc hệ thống. Tôi cần chủ động trao đổi nhiều hơn khi gặp các vấn đề kỹ thuật phức tạp. |
| 8 | **Tư duy giải quyết vấn đề** | Tốt | Trong quá trình triển khai, tôi biết chia nhỏ bài toán thành các thành phần độc lập như huấn luyện mô hình, triển khai endpoint, xử lý streaming, cảnh báo và lưu trữ dữ liệu để dễ dàng kiểm thử và xử lý lỗi. |
| 9 | **Khả năng sử dụng công cụ** | Tốt | Tôi sử dụng thành thạo AWS Console, Hugo, Markdown và Git để triển khai hệ thống, xây dựng tài liệu và quản lý nội dung project. |
| 10 | **Đóng góp vào project cá nhân** | Tốt | Tôi đã xây dựng hoàn chỉnh một hệ thống Fraud Detection có đầy đủ quy trình từ huấn luyện, triển khai, dự đoán thời gian thực, cảnh báo và lưu trữ dữ liệu, đồng thời hoàn thiện tài liệu hướng dẫn triển khai. |
| 11 | **Khả năng tự đánh giá và cải thiện** | Tốt | Tôi thường xuyên rà soát lại kiến trúc hệ thống, cập nhật tài liệu, bổ sung hình ảnh minh chứng và tối ưu quy trình triển khai để báo cáo được đầy đủ và chính xác hơn. |
| 12 | **Đánh giá tổng thể** | Tốt | Tôi đã đạt được mục tiêu xây dựng thành công hệ thống phát hiện gian lận trên AWS, đồng thời hiểu rõ quy trình triển khai Machine Learning trên môi trường Cloud từ dữ liệu đến vận hành thực tế. |

## Điểm mạnh đạt được

- Hiểu rõ quy trình xây dựng và triển khai một hệ thống Machine Learning trên AWS.
- Thiết kế được kiến trúc gồm Training Zone và Real-time Zone theo mô hình xử lý dữ liệu thực tế.
- Thành thạo hơn trong việc sử dụng các dịch vụ Amazon S3, SageMaker, API Gateway, Lambda, Kinesis, SNS và Firehose.
- Biết cách triển khai mô hình Machine Learning dưới dạng SageMaker Real-time Endpoint.
- Hiểu cách xây dựng pipeline xử lý dữ liệu streaming và tích hợp nhiều dịch vụ AWS trong cùng một hệ thống.
- Có khả năng xây dựng tài liệu kỹ thuật và website hướng dẫn bằng Hugo để mô tả toàn bộ quy trình triển khai.

## Điểm cần cải thiện

- Tiếp tục tìm hiểu sâu hơn về tối ưu hiệu năng và khả năng mở rộng của hệ thống khi xử lý lưu lượng giao dịch lớn.
- Nâng cao kỹ năng tối ưu chi phí vận hành, đặc biệt đối với SageMaker Endpoint và các dịch vụ xử lý dữ liệu thời gian thực.
- Thực hiện thêm các kịch bản kiểm thử với dữ liệu lớn nhằm đánh giá độ ổn định của hệ thống.
- Nghiên cứu bổ sung các giải pháp giám sát và bảo mật nâng cao cho hệ thống Machine Learning trên AWS.

## Kế hoạch phát triển trong thời gian tới

Trong thời gian tới, tôi sẽ tiếp tục phát triển project theo các hướng sau:

1. Thử nghiệm thêm nhiều thuật toán Machine Learning và Deep Learning để nâng cao độ chính xác của mô hình.
2. Xây dựng cơ chế tự động huấn luyện và triển khai lại mô hình (MLOps) khi có dữ liệu mới.
3. Bổ sung Dashboard giám sát kết quả dự đoán và hiệu năng hệ thống.
4. Tìm hiểu thêm về CI/CD và Infrastructure as Code để tự động hóa quá trình triển khai trên AWS.
5. Tiếp tục nâng cao kỹ năng tiếng Anh chuyên ngành nhằm đọc hiểu tài liệu kỹ thuật và các dịch vụ AWS mới.

## Kết luận tự đánh giá

Qua quá trình thực hiện project, tôi đã có cơ hội kết hợp kiến thức về Machine Learning với các dịch vụ Cloud để xây dựng một hệ thống phát hiện gian lận giao dịch thẻ tín dụng theo kiến trúc gần với thực tế doanh nghiệp. Project giúp tôi hiểu rõ hơn quy trình triển khai một hệ thống AI từ lưu trữ dữ liệu, huấn luyện mô hình, triển khai endpoint, xử lý dữ liệu thời gian thực, gửi cảnh báo đến lưu trữ kết quả và quản lý tài nguyên trên AWS.

Tôi tự đánh giá kết quả thực tập ở mức **Tốt**. Project đã giúp tôi củng cố kiến thức chuyên môn, nâng cao kỹ năng triển khai hệ thống Machine Learning trên nền tảng Cloud và tạo nền tảng để tiếp tục nghiên cứu các giải pháp MLOps và AI quy mô lớn trong tương lai.