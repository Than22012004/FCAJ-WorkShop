# Báo cáo Workshop: Phát hiện gian lận thẻ tín dụng (Realtime ML on AWS)

Tổng hợp quá trình thực hiện workshop, mục tiêu, kiến trúc, các bước triển khai và lưu ý clean-up.

> Generated from workspace content/5-Workshop (Vietnamese sections)

---

## Tổng quan

Trong workshop này, chúng ta sẽ xây dựng một hệ thống **phát hiện gian lận thẻ tín dụng theo thời gian thực** bằng cách kết hợp Machine Learning và các dịch vụ AWS.

Hệ thống được thiết kế theo hai phần chính:

- **Training Zone:** chuẩn bị dữ liệu, huấn luyện mô hình Machine Learning, đóng gói model và triển khai SageMaker Real-time Endpoint.
- **Real-time Zone:** nhận giao dịch từ User hoặc Banking System, xử lý dữ liệu theo luồng realtime, gọi model để dự đoán Fraud/Normal, gửi cảnh báo nếu phát hiện giao dịch nghi ngờ và lưu lịch sử prediction.

### Mục tiêu workshop

Sau khi hoàn thành workshop, bạn có thể:

- Tạo Amazon S3 Data Lake để lưu dữ liệu giao dịch, feature, dataset train/test, model artifact và prediction history.
- Huấn luyện mô hình **Random Forest** bằng Amazon SageMaker.
- Đóng gói các file `model.joblib`, `scaler.joblib`, `inference.py` thành `model.tar.gz`.
- Triển khai model thành **SageMaker Real-time Endpoint**.
- Xây dựng API nhận giao dịch bằng Amazon API Gateway.
- Sử dụng AWS Lambda để parse JSON, validate dữ liệu, chuẩn hóa dữ liệu và đưa transaction vào Kinesis.
- Sử dụng Amazon Kinesis để tiếp nhận stream giao dịch realtime.
- Sử dụng Lambda Read Features để feature engineering, mapping feature và gọi SageMaker Endpoint.
- Gửi cảnh báo qua Amazon SNS đến Email Admin khi phát hiện Fraud.
- Lưu prediction result xuống Amazon S3 thông qua Kinesis Firehose.
- Theo dõi log/metric bằng Amazon CloudWatch.
- Clean-up tài nguyên để tránh phát sinh chi phí.

---

## Nội dung chi tiết (từ các mục workshop)

### 1. Tổng quan về workshop (5.1)

Gian lận thẻ tín dụng là một bài toán quan trọng trong các hệ thống thanh toán điện tử. Một giao dịch gian lận nếu không được phát hiện kịp thời có thể gây thiệt hại tài chính, ảnh hưởng đến uy tín của tổ chức và làm giảm mức độ tin cậy của người dùng đối với hệ thống.

Trong thực tế, các hệ thống phát hiện gian lận thường cần xử lý giao dịch gần như theo thời gian thực. Khi một giao dịch mới xuất hiện, hệ thống cần nhanh chóng đánh giá mức độ rủi ro, xác định giao dịch là bình thường hay nghi ngờ gian lận, sau đó gửi cảnh báo cho người quản trị nếu cần.

Workshop này mô phỏng một hệ thống như vậy bằng cách sử dụng Machine Learning và các dịch vụ AWS.

Mục tiêu, kiến trúc, dữ liệu đầu vào/đầu ra và các lưu ý an toàn được trình bày trong phần này.

### 2. Chuẩn bị (5.2)

Trước khi triển khai workshop phát hiện gian lận thẻ tín dụng bằng Machine Learning trên AWS, cần chuẩn bị tài khoản AWS, region, quyền IAM, dataset mẫu, email nhận cảnh báo và một số công cụ hỗ trợ.

- Account: `ThanPham`
- Region: `ap-southeast-1` (Asia Pacific Singapore)
- Dataset (local): `E:\aws\dataset\creditcard.csv`
- Emails nhận alert: `lehoanggiavi21082004@gmail.com`, `thanpham2k4@gmail.com`

Thư viện Python cần có: `pandas`, `numpy`, `scikit-learn`, `joblib`, `boto3`.

### 3. Chuẩn bị dữ liệu và S3 Data Lake (5.3)

Mục tiêu: tạo S3 bucket, cấu trúc Data Lake và tải dataset `creditcard.csv` vào prefix `raw/`.

Cấu trúc đề xuất:

```
s3://<bucket-name>/raw/
s3://<bucket-name>/data_train/
s3://<bucket-name>/model/
s3://<bucket-name>/model.tar.gz
```

### 3.1 Tạo S3 bucket và cấu trúc (5.3.1)

Hướng dẫn tạo bucket, cấu hình quyền, đặt tên bucket duy nhất và tạo các prefix `raw/`, `data_train/`, `model/`.

### 3.2 Tải dataset và kiểm tra (5.3.2)

Hướng dẫn upload file `creditcard.csv` lên `raw/` bằng S3 Console và kiểm tra object `raw/creditcard.csv`.

### 4. Huấn luyện model và triển khai SageMaker Endpoint (5.4)

Quy trình:

- Chuẩn bị môi trường train (SageMaker Notebook/Studio hoặc local). Thư viện cần: pandas, numpy, scikit-learn, joblib, boto3.
- Đọc dữ liệu từ S3, preprocessing, feature engineering, tách train/test, train Random Forest.
- Lưu artifact: `model.joblib`, `scaler.joblib`.
- Tạo `inference.py` và đóng gói `model.tar.gz`.
- Tạo SageMaker model và Real-time Endpoint (trạng thái `InService`).
- Kiểm tra endpoint bằng request mẫu.

### 5. Realtime pipeline, alert và lưu lịch sử (5.5)

Các thành phần chính:

- API Gateway: nhận request giao dịch.
- Lambda ingest: parse JSON, validate input, đưa record vào Kinesis.
- Kinesis Data Streams: buffer luồng giao dịch.
- Lambda Read Features: mapping feature, gọi SageMaker Endpoint.
- SageMaker Endpoint: trả về prediction và probability.
- SNS: gửi email alert khi phát hiện Fraud.
- Firehose: ghi prediction history xuống S3.
- CloudWatch: theo dõi log/metric.

Request mẫu và response kỳ vọng được mô tả trong tài liệu gốc.

### 6. Clean-up (5.6)

Bước quan trọng: xóa SageMaker Real-time Endpoint sau khi demo để tránh chi phí. Các tài nguyên khác (S3, Lambda, Kinesis, Firehose, SNS, CloudWatch, IAM) được giữ lại cho báo cáo.

---

## Tệp đính kèm và minh họa

Các hình ảnh minh họa, sơ đồ pipeline và ảnh chụp màn hình được giữ nguyên dưới dạng link gốc trong tài liệu nguồn (workshop images).

---

## Footer

File này được tạo tự động từ nội dung trong thư mục `content/5-Workshop` (Vietnamese). Nếu bạn muốn bản tiếng Anh hoặc phiên bản rút gọn/đầy đủ hơn, cho tôi biết để tạo thêm phiên bản PDF tương ứng.
