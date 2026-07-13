# Báo cáo thực tập

## Mở đầu

Trong bối cảnh chuyển đổi số diễn ra mạnh mẽ trên toàn cầu, các doanh nghiệp và tổ chức ngày càng chú trọng đến việc tận dụng công nghệ để nâng cao hiệu quả vận hành, tăng cường bảo mật và cải thiện trải nghiệm người dùng. Trong số những công nghệ nổi bật hiện nay, điện toán đám mây và trí tuệ nhân tạo là hai lĩnh vực có ảnh hưởng lớn đến cách các hệ thống được thiết kế, triển khai và vận hành. Chính vì vậy, việc tham gia một đợt thực tập liên quan đến nền tảng AWS và các giải pháp AI/ML đã mang lại cho em một trải nghiệm học tập vô cùng quý giá.

Em đã có cơ hội tham gia chương trình thực tập tại Công ty TNHH Amazon Web Services Việt Nam với đề tài thực hiện là xây dựng một hệ thống phát hiện gian lận giao dịch theo thời gian thực trên nền tảng AWS. Dự án này không chỉ giúp em củng cố kiến thức về Machine Learning, Cloud Computing và kiến trúc hệ thống mà còn tạo điều kiện để em hiểu rõ hơn về quy trình làm việc thực tế trong môi trường công nghệ hiện đại. Bài báo cáo này nhằm trình bày toàn bộ quá trình thực tập, từ giới thiệu về đơn vị, nội dung công việc được phân công, phương pháp thực hiện cho đến kết quả đạt được và những bài học rút ra sau đợt thực tập.

## 2.1. Giới thiệu về đơn vị thực tập

Đơn vị thực tập của em là Công ty TNHH Amazon Web Services Việt Nam, nơi em tham gia chương trình Workforce Bootcamp - First Cloud AI Journey. Đây là một môi trường học tập và làm việc gắn với các lĩnh vực công nghệ mũi nhọn, đặc biệt là điện toán đám mây, trí tuệ nhân tạo, phân tích dữ liệu và phát triển ứng dụng. AWS là một trong những nền tảng hàng đầu thế giới về dịch vụ cloud, cung cấp cho doanh nghiệp các công cụ để xây dựng hệ thống có khả năng mở rộng, bảo mật cao và vận hành hiệu quả.

Về lĩnh vực hoạt động, AWS tập trung vào việc cung cấp các giải pháp hạ tầng và nền tảng công nghệ cho doanh nghiệp, tổ chức giáo dục, startup và các đơn vị nghiên cứu phát triển. Các dịch vụ của AWS bao phủ nhiều khía cạnh của công nghệ hiện đại như lưu trữ dữ liệu, điện toán, mạng, phân tích dữ liệu, bảo mật, máy học, trí tuệ nhân tạo và vận hành tự động. Với mô hình dịch vụ linh hoạt, người dùng có thể lựa chọn và kết hợp nhiều dịch vụ khác nhau để xây dựng giải pháp phù hợp với nhu cầu cụ thể của mình.

Trong bối cảnh công nghệ ngày càng phát triển, các doanh nghiệp đang có nhu cầu chuyển đổi sang nền tảng cloud để tối ưu chi phí, tăng tốc độ triển khai và nâng cao độ tin cậy của hệ thống. AWS đã trở thành lựa chọn ưu tiên của nhiều tổ chức bởi khả năng cung cấp dịch vụ ổn định, dễ mở rộng và hỗ trợ tốt cho các ứng dụng quy mô lớn. Qua đợt thực tập, em nhận thấy rằng việc hiểu và vận hành các dịch vụ cloud không chỉ dừng lại ở lý thuyết mà còn đòi hỏi người làm việc phải có tư duy hệ thống, khả năng học hỏi và kỹ năng giải quyết vấn đề thực tế.

Về lịch sử hình thành và phát triển, AWS là một phần trong hệ sinh thái công nghệ của Amazon, được xây dựng và phát triển từ các nền tảng điện toán đám mây đầu tiên, sau đó mở rộng sang nhiều lĩnh vực như AI/ML, phân tích dữ liệu, bảo mật và Internet of Things. Quá trình phát triển này cho thấy AWS không chỉ là một nhà cung cấp dịch vụ công nghệ mà còn là một trung tâm đổi mới, nơi các giải pháp mới liên tục được tạo ra để đáp ứng nhu cầu đa dạng của thị trường. Tại Việt Nam, AWS đang thúc đẩy chuyển đổi số thông qua việc cung cấp kiến thức, công cụ và nền tảng để người học và doanh nghiệp tiếp cận công nghệ hiện đại một cách hiệu quả hơn.

Về cơ cấu tổ chức hành chính, đơn vị hoạt động theo mô hình chuyên môn hóa, trong đó các nhóm làm việc được phân theo nhiệm vụ và lĩnh vực cụ thể như kỹ thuật, giải pháp, đào tạo, hỗ trợ khách hàng và vận hành. Mỗi nhóm có vai trò riêng nhưng luôn cần phối hợp chặt chẽ để triển khai các hoạt động chuyên môn hiệu quả. Đây là môi trường rất phù hợp cho sinh viên như em để hiểu cách làm việc chuyên nghiệp trong môi trường công nghệ, biết cách giao tiếp, chia sẻ nhiệm vụ và phối hợp để hoàn thành mục tiêu chung.

Các hoạt động chuyên môn gắn liền với lĩnh vực thực tập của em chủ yếu xoay quanh việc nghiên cứu, triển khai và vận hành các dịch vụ AWS phục vụ cho bài toán phát hiện gian lận giao dịch theo thời gian thực. Trong quá trình thực tập, em được tiếp cận với các công cụ và dịch vụ như Amazon S3, AWS Lambda, Amazon SageMaker, Amazon API Gateway, Amazon Kinesis, Amazon SNS, Kinesis Firehose và Amazon CloudWatch. Những dịch vụ này không hoạt động riêng lẻ mà được kết hợp với nhau để tạo thành một hệ thống hoàn chỉnh, từ thu thập dữ liệu, tiền xử lý, huấn luyện mô hình, triển khai prediction, gửi cảnh báo cho đến lưu trữ kết quả.

Môi trường làm việc trong đợt thực tập rất năng động, chuyên nghiệp và tạo điều kiện cho người học phát triển toàn diện. Em được khuyến khích chủ động nghiên cứu, thử nghiệm, ghi nhận kết quả và trao đổi với người hướng dẫn khi gặp khó khăn. Đây là một môi trường phù hợp để rèn luyện tính chủ động, sự cẩn thận, khả năng tự học và thái độ làm việc trách nhiệm. Những trải nghiệm này không chỉ có giá trị trong quá trình thực tập mà còn là nền tảng vững chắc cho công việc sau này.

## 2.2. Nội dung công việc được phân công

Trong suốt thời gian thực tập, em được phân công tham gia vào một dự án cá nhân với mục tiêu xây dựng hệ thống phát hiện gian lận giao dịch trên nền tảng AWS. Đây là một đề tài phù hợp với lĩnh vực Data Science, Machine Learning và Cloud Engineering, đồng thời cho phép em kết nối giữa kiến thức học ở trường với ứng dụng thực tế trong môi trường doanh nghiệp. Dự án được triển khai dưới hình thức một workshop và báo cáo thực tập, mang tính chất học thuật nhưng có yếu tố thực tế và có thể áp dụng vào các tình huống sản phẩm thực tế.

Các nội dung công việc được phân công có tính hệ thống và được chia theo từng giai đoạn rõ ràng như sau:

### 2.2.1. Nghiên cứu và phân tích bài toán

Đây là bước đầu tiên và có vai trò rất quan trọng trong toàn bộ dự án. Em cần hiểu rõ bản chất của bài toán phát hiện gian lận giao dịch, các loại giao dịch có thể bị nghi ngờ, các dấu hiệu bất thường và các yêu cầu kỹ thuật để xây dựng một hệ thống có thể phát hiện hành vi gian lận trong thời gian thực. Trong quá trình nghiên cứu, em tìm hiểu các khái niệm về fraud detection, dữ liệu giao dịch, feature engineering, mô hình phân loại và cách đánh giá hiệu quả của mô hình bằng các chỉ số như Precision, Recall và F1-score.

### 2.2.2. Thiết kế kiến trúc hệ thống

Sau khi hiểu được bài toán, em tiến hành thiết kế kiến trúc hệ thống theo mô hình Training Zone và Real-time Zone. Training Zone bao gồm các công đoạn chuẩn bị dữ liệu, tiền xử lý, huấn luyện mô hình và triển khai model endpoint. Real-time Zone bao gồm các bước tiếp nhận giao dịch, xử lý dữ liệu streaming, gọi model để dự đoán, gửi cảnh báo và lưu trữ kết quả. Việc thiết kế kiến trúc giúp em hiểu được cách các dịch vụ AWS phối hợp với nhau để tạo thành một hệ thống end-to-end.

### 2.2.3. Chuẩn bị dữ liệu và xây dựng mô hình

Một phần quan trọng trong dự án là chuẩn bị dữ liệu và xây dựng mô hình Machine Learning phù hợp. Em nghiên cứu cách thu thập và tổ chức dữ liệu giao dịch mẫu, làm sạch dữ liệu, xử lý các trường dữ liệu thiếu hoặc bất thường, và chuyển đổi dữ liệu sang định dạng phù hợp cho huấn luyện mô hình. Quá trình này bao gồm việc xác định các feature quan trọng như số tiền giao dịch, thời điểm giao dịch, loại giao dịch, vị trí, thiết bị, và các yếu tố liên quan khác. Sau đó, mô hình Random Forest được lựa chọn cho bài toán phân loại vì tính dễ triển khai và phù hợp với dữ liệu dạng bảng.

### 2.2.4. Triển khai dịch vụ trên AWS

Sau khi huấn luyện mô hình, em tiến hành triển khai mô hình lên SageMaker Real-time Endpoint. Đồng thời, em thực hiện xây dựng pipeline realtime bằng cách kết nối API Gateway và Lambda để nhận dữ liệu giao dịch từ phía người dùng hoặc hệ thống giả lập. Dữ liệu được đưa vào Amazon Kinesis, sau đó được xử lý bởi Lambda Read Features để chuẩn hóa và tạo input phù hợp cho mô hình. Nếu kết quả dự đoán là Fraud thì hệ thống gửi cảnh báo qua Amazon SNS và lưu lịch sử dự đoán xuống Amazon S3 thông qua Kinesis Firehose.

### 2.2.5. Tài liệu hóa và trình bày kết quả

Ngoài việc triển khai hệ thống, em cũng được giao nhiệm vụ tổng hợp toàn bộ quá trình thực hiện thành các tài liệu báo cáo, worklog, blog và nội dung website bằng Hugo. Đây là một phần quan trọng vì nó cho thấy việc xây dựng một dự án kỹ thuật không chỉ dừng lại ở code và triển khai mà còn cần có cách trình bày, tài liệu hóa và chia sẻ kiến thức rõ ràng cho người khác tham khảo.

### 2.2.6. Kiểm thử, tối ưu và dọn dẹp tài nguyên

Một phần không thể thiếu trong quy trình làm việc là kiểm thử và tối ưu chi phí. Em cần theo dõi hoạt động của endpoint, log của Lambda, dữ liệu lưu trong Kinesis và các cảnh báo từ SNS. Đồng thời, em cũng cần thực hiện các bước clean-up sau khi hoàn thành bài thực hành để tránh phát sinh chi phí không cần thiết. Đây là một bài học thực tế rất có giá trị vì trong môi trường cloud, tài nguyên cần được quản lý cẩn thận và có trách nhiệm.

## 2.3. Nhật ký công việc theo tuần

Dưới đây là nhật ký chi tiết các công việc đã thực hiện trong 12 tuần thực tập, phản ánh quá trình xây dựng hệ thống phát hiện gian lận giao dịch theo thời gian thực trên AWS.

### Tuần 1 (17/04 – 25/04)

**Mục tiêu:**
- Tham gia chương trình Bootcamp First Cloud AI Journey.
- Làm quen với mentor, quy trình làm việc và môi trường AWS.
- Tìm hiểu yêu cầu dự án và khảo sát kiến trúc tổng quan hệ thống Machine Learning trên AWS.

**Công việc đã thực hiện:**
- Tham gia chương trình Bootcamp First Cloud AI Journey.
- Làm quen với mentor, quy trình làm việc và môi trường AWS.
- Tìm hiểu yêu cầu của dự án phát hiện giao dịch gian lận thời gian thực.
- Khảo sát kiến trúc tổng quan của hệ thống Machine Learning trên nền tảng AWS.

**Kết quả đạt được:**
- Nắm được yêu cầu tổng thể của chương trình thực tập và quy trình làm việc tại công ty.
- Hiểu vai trò cơ bản của các dịch vụ AWS sẽ được dùng trong project.
- Xác định được chủ đề project cá nhân: Real-time Fraud Detection System using Machine Learning on AWS.
- Có định hướng ban đầu cho pipeline gồm hai phần: training model và realtime inference.

### Tuần 2 (27/04 – 03/05)

**Mục tiêu:**
- Nghiên cứu các dịch vụ AWS sử dụng trong dự án.
- Tìm hiểu kiến trúc Data Lake và quy trình triển khai mô hình ML trên AWS.
- Xây dựng kế hoạch triển khai dự án.

**Công việc đã thực hiện:**
- Nghiên cứu các dịch vụ AWS sử dụng trong dự án gồm Amazon S3, SageMaker, Lambda, API Gateway, Kinesis Data Streams, Kinesis Firehose và Amazon SNS.
- Tìm hiểu kiến trúc Data Lake trên Amazon S3 và quy trình triển khai mô hình Machine Learning trên AWS.
- Xây dựng kế hoạch triển khai dự án và phân chia các giai đoạn thực hiện.

**Kết quả đạt được:**
- Hiểu rõ vai trò của từng dịch vụ AWS trong bài toán fraud detection.
- Nắm vững kiến trúc Data Lake trên Amazon S3 và quy trình triển khai ML trên AWS.
- Có bản kế hoạch triển khai dự án chi tiết với các giai đoạn rõ ràng.
- Có bản phác thảo kiến trúc đầu tiên: Training Pipeline và Realtime Inference Pipeline.

### Tuần 3 (04/05 – 10/05)

**Mục tiêu:**
- Thu thập bộ dữ liệu giao dịch thẻ tín dụng phục vụ huấn luyện mô hình.
- Phân tích và tiền xử lý dữ liệu.
- Lưu dữ liệu huấn luyện lên Amazon S3.

**Công việc đã thực hiện:**
- Thu thập bộ dữ liệu giao dịch thẻ tín dụng phục vụ huấn luyện mô hình.
- Phân tích dữ liệu, kiểm tra dữ liệu thiếu và dữ liệu mất cân bằng.
- Tiền xử lý dữ liệu: chuẩn hóa dữ liệu, lựa chọn đặc trưng (Feature Engineering), chia tập Train/Test.
- Lưu dữ liệu huấn luyện lên Amazon S3 để phục vụ SageMaker.

**Kết quả đạt được:**
- Thu thập thành công bộ dữ liệu giao dịch thẻ tín dụng (creditcard.csv).
- Phân tích được đặc điểm dữ liệu: tỷ lệ mất cân bằng, dữ liệu thiếu.
- Hoàn thành tiền xử lý: chuẩn hóa, Feature Engineering, chia tập Train/Test.
- Dữ liệu huấn luyện đã được lưu trữ trên Amazon S3, sẵn sàng cho SageMaker.

### Tuần 4 (11/05 – 17/05)

**Mục tiêu:**
- Thiết kế kiến trúc tổng thể của hệ thống.
- Thiết kế luồng dữ liệu và cơ chế cảnh báo.
- Chuẩn bị môi trường AWS và cấu hình IAM Role.

**Công việc đã thực hiện:**
- Thiết kế kiến trúc tổng thể của hệ thống gồm Training Zone và Real-time Inference Zone.
- Thiết kế luồng dữ liệu từ API Gateway → Lambda → Kinesis → SageMaker Endpoint → Firehose → Amazon S3.
- Thiết kế cơ chế gửi cảnh báo thông qua Amazon SNS khi phát hiện giao dịch gian lận.
- Chuẩn bị môi trường AWS và cấu hình IAM Role cho các dịch vụ.

**Kết quả đạt được:**
- Hoàn thành thiết kế kiến trúc tổng thể với hai zone: Training và Real-time Inference.
- Xác định rõ luồng dữ liệu end-to-end từ API Gateway đến Amazon S3.
- Thiết kế xong cơ chế gửi cảnh báo qua Amazon SNS.
- Môi trường AWS và IAM Role đã được cấu hình, sẵn sàng triển khai.

### Tuần 5 (18/05 – 24/05)

**Mục tiêu:**
- Xây dựng Notebook trên Amazon SageMaker.
- Huấn luyện mô hình Random Forest và đánh giá hiệu năng.
- Lựa chọn mô hình tối ưu để triển khai.

**Công việc đã thực hiện:**
- Xây dựng Notebook trên Amazon SageMaker.
- Huấn luyện mô hình Random Forest bằng Scikit-learn.
- Tinh chỉnh tham số mô hình và đánh giá hiệu năng thông qua Accuracy, Precision, Recall, F1-score và Confusion Matrix.
- Lựa chọn mô hình tối ưu để triển khai.

**Kết quả đạt được:**
- Huấn luyện thành công mô hình Random Forest trên Amazon SageMaker.
- Đạt kết quả tốt trên tập test: Accuracy >99%, Recall >80%, F1-score >85%.
- Xác định mô hình phù hợp nhất để triển khai.
- Lưu mô hình xuống file model.pkl, sẵn sàng đóng gói.

### Tuần 6 (25/05 – 31/05)

**Mục tiêu:**
- Đóng gói mô hình và viết file inference.py.
- Upload mô hình lên Amazon S3.
- Triển khai SageMaker Real-time Endpoint và kiểm thử.

**Công việc đã thực hiện:**
- Đóng gói mô hình thành file model.tar.gz.
- Viết file inference.py phục vụ suy luận thời gian thực.
- Upload mô hình lên Amazon S3.
- Triển khai mô hình dưới dạng Amazon SageMaker Real-time Endpoint.
- Kiểm thử Endpoint bằng dữ liệu mẫu và đánh giá thời gian phản hồi.

**Kết quả đạt được:**
- Đóng gói mô hình thành công dưới dạng model.tar.gz.
- Hoàn thành inference.py với đầy đủ hàm model_fn, input_fn, predict_fn, output_fn.
- Upload mô hình lên Amazon S3 và triển khai SageMaker Endpoint thành công.
- Endpoint hoạt động ổn định với thời gian phản hồi đạt yêu cầu cho realtime.

### Tuần 7 (01/06 – 07/06)

**Mục tiêu:**
- Xây dựng REST API bằng Amazon API Gateway.
- Phát triển AWS Lambda tiếp nhận dữ liệu.
- Chuẩn hóa dữ liệu và gửi vào Amazon Kinesis Data Streams.

**Công việc đã thực hiện:**
- Xây dựng REST API bằng Amazon API Gateway để tiếp nhận giao dịch.
- Phát triển AWS Lambda tiếp nhận dữ liệu từ API Gateway.
- Chuẩn hóa dữ liệu đầu vào và gửi dữ liệu vào Amazon Kinesis Data Streams.
- Kiểm thử việc truyền dữ liệu từ Client đến Kinesis.

**Kết quả đạt được:**
- API hoạt động ổn định, tiếp nhận dữ liệu giao dịch qua POST method.
- Lambda nhận được event từ API Gateway, chuẩn hóa dữ liệu thành công.
- Dữ liệu giao dịch đã truyền được từ Client đến Kinesis Data Streams.
- Sẵn sàng cho bước tiếp theo: Lambda xử lý stream và gọi SageMaker.

### Tuần 8 (08/06 – 14/06)

**Mục tiêu:**
- Cấu hình Amazon Kinesis Data Streams phục vụ xử lý dữ liệu thời gian thực.
- Xây dựng Lambda đọc dữ liệu từ Stream.
- Thực hiện Feature Engineering trên dữ liệu streaming và gửi đến SageMaker Endpoint.

**Công việc đã thực hiện:**
- Cấu hình Amazon Kinesis Data Streams phục vụ xử lý dữ liệu thời gian thực.
- Xây dựng Lambda đọc dữ liệu từ Stream.
- Thực hiện Feature Engineering trên dữ liệu streaming.
- Gửi dữ liệu đã xử lý đến SageMaker Endpoint để dự đoán giao dịch.

**Kết quả đạt được:**
- Kinesis Data Streams hoạt động ổn định phục vụ xử lý dữ liệu thời gian thực.
- Lambda đọc thành công các record từ Kinesis Data Streams.
- Feature Engineering trên streaming data hoạt động ổn định.
- Gọi SageMaker Endpoint trong Lambda và nhận kết quả dự đoán thành công.

### Tuần 9 (15/06 – 21/06)

**Mục tiêu:**
- Tích hợp SageMaker Endpoint với pipeline xử lý dữ liệu thời gian thực.
- Phân loại giao dịch hợp lệ và giao dịch gian lận.
- Kiểm thử và đánh giá độ ổn định của hệ thống.

**Công việc đã thực hiện:**
- Tích hợp SageMaker Endpoint với pipeline xử lý dữ liệu thời gian thực.
- Phân loại giao dịch hợp lệ và giao dịch gian lận.
- Kiểm thử khả năng dự đoán liên tục với dữ liệu mô phỏng.
- Đánh giá độ ổn định của hệ thống và thời gian xử lý từng giao dịch.

**Kết quả đạt được:**
- SageMaker Endpoint tích hợp thành công với pipeline xử lý dữ liệu thời gian thực.
- Hệ thống phân loại chính xác giao dịch hợp lệ (prediction = 0) và gian lận (prediction = 1).
- Kiểm thử dự đoán liên tục với dữ liệu mô phỏng cho kết quả ổn định.
- Pipeline Kinesis → Lambda → SageMaker hoàn chỉnh, sẵn sàng tích hợp SNS và Firehose.

### Tuần 10 (22/06 – 28/06)

**Mục tiêu:**
- Cấu hình Amazon SNS gửi cảnh báo khi phát hiện giao dịch gian lận.
- Thiết lập Amazon Kinesis Firehose lưu lịch sử giao dịch.
- Kiểm thử luồng dữ liệu hoàn chỉnh và khả năng mở rộng.

**Công việc đã thực hiện:**
- Cấu hình Amazon SNS gửi email cảnh báo khi phát hiện giao dịch gian lận.
- Thiết lập Amazon Kinesis Firehose lưu toàn bộ lịch sử giao dịch vào Amazon S3.
- Kiểm thử luồng dữ liệu hoàn chỉnh từ API Gateway đến Amazon S3.
- Kiểm tra cơ chế lưu trữ và khả năng mở rộng của hệ thống.

**Kết quả đạt được:**
- SNS gửi email cảnh báo thành công khi phát hiện giao dịch gian lận.
- Kinesis Firehose lưu lịch sử giao dịch vào S3 ổn định.
- Kiểm thử thành công luồng dữ liệu end-to-end: API Gateway → Lambda → Kinesis → SageMaker → SNS/Firehose → S3.
- Hệ thống realtime fraud detection cơ bản hoàn chỉnh.

### Tuần 11 (29/06 – 05/07)

**Mục tiêu:**
- Tối ưu chi phí sử dụng các dịch vụ AWS.
- Thiết lập Amazon CloudWatch giám sát hệ thống.
- Đánh giá khả năng mở rộng và hoàn thiện Workshop.

**Công việc đã thực hiện:**
- Tối ưu chi phí sử dụng các dịch vụ AWS bằng cách dừng Endpoint và Stream khi không sử dụng.
- Thiết lập Amazon CloudWatch để theo dõi hoạt động của Lambda và SageMaker Endpoint.
- Đánh giá khả năng mở rộng, tính sẵn sàng và độ tin cậy của hệ thống.
- Hoàn thiện Workshop và cập nhật tài liệu kỹ thuật của dự án.

**Kết quả đạt được:**
- Xác định được các bước tối ưu chi phí: tắt Endpoint và Stream khi không sử dụng.
- CloudWatch giám sát thành công các Lambda function và SageMaker Endpoint.
- Đánh giá hoàn chỉnh khả năng mở rộng, tính sẵn sàng và độ tin cậy của hệ thống.
- Workshop và tài liệu kỹ thuật của dự án được hoàn thiện và cập nhật.

### Tuần 12 (06/07 – 12/07)

**Mục tiêu:**
- Kiểm thử End-to-End toàn bộ hệ thống.
- Đánh giá kết quả và phân tích ưu nhược điểm.
- Hoàn thiện báo cáo thực tập và chuẩn bị demo hệ thống.

**Công việc đã thực hiện:**
- Kiểm thử End-to-End toàn bộ hệ thống với nhiều kịch bản giao dịch.
- Đánh giá kết quả đạt được và phân tích ưu, nhược điểm của giải pháp.
- Hoàn thiện báo cáo thực tập, sơ đồ kiến trúc và tài liệu hướng dẫn triển khai.
- Chuẩn bị báo cáo, demo hệ thống.

**Kết quả đạt được:**
- Kiểm thử End-to-End thành công với nhiều kịch bản: giao dịch hợp lệ, giao dịch gian lận và edge case.
- Đánh giá hoàn chỉnh kết quả đạt được và phân tích rõ ưu, nhược điểm của giải pháp.
- Hoàn thiện báo cáo thực tập, sơ đồ kiến trúc và tài liệu hướng dẫn triển khai.
- Sẵn sàng báo cáo và demo hệ thống.

## 2.4. Phương pháp thực hiện

Để hoàn thành các nhiệm vụ được giao một cách hiệu quả, em đã áp dụng phương pháp làm việc tuần tự, có hệ thống và tập trung vào hiểu bản chất công nghệ trước khi triển khai. Phương pháp này không chỉ giúp em hoàn thành công việc đúng tiến độ mà còn rèn luyện được tư duy logic, kỹ năng giải quyết vấn đề và thái độ làm việc chuyên nghiệp.

### 2.4.1. Nghiên cứu tài liệu và tiếp cận kiến thức nền tảng

Trước khi bắt đầu triển khai, em dành thời gian nghiên cứu các tài liệu liên quan đến AWS, Machine Learning, kiến trúc hệ thống và quy trình xử lý dữ liệu thời gian thực. Quá trình này giúp em nắm được các khái niệm cơ bản, cách hoạt động của từng dịch vụ và mối liên hệ giữa các thành phần trong hệ thống. Em cũng tham khảo các ví dụ thực tế, tài liệu chính thức của AWS và các nội dung từ workshop để có cái nhìn toàn diện hơn về project.

### 2.4.2. Phân tích yêu cầu và chia nhỏ công việc

Sau khi có nền tảng kiến thức, em tiến hành phân tích yêu cầu của dự án và chia công việc thành từng giai đoạn. Việc chia nhỏ công việc giúp giảm áp lực, dễ kiểm soát tiến độ và phát hiện lỗi sớm hơn. Các giai đoạn chính bao gồm nghiên cứu, thiết kế kiến trúc, chuẩn bị dữ liệu, huấn luyện mô hình, triển khai endpoint, xây dựng pipeline realtime, kiểm thử và hoàn thiện báo cáo.

### 2.4.3. Triển khai từng bước và kiểm tra liên tục

Trong suốt quá trình thực hiện, em không triển khai toàn bộ hệ thống một cách đồng loạt mà làm theo từng phần nhỏ. Ví dụ, đầu tiên em nghiên cứu và thiết kế Training Zone; sau đó mới triển khai Real-time Zone; cuối cùng mới tích hợp các thành phần vào một pipeline hoàn chỉnh. Mỗi bước đều được kiểm tra kỹ càng để đảm bảo kết quả đầu ra chính xác và hệ thống hoạt động ổn định.

### 2.4.4. Ghi nhận kết quả và tổng hợp kinh nghiệm

Một yếu tố rất quan trọng trong quy trình làm việc là ghi chép lại các bước thực hiện, vấn đề gặp phải và cách giải quyết. Em đã lưu lại các nội dung này trong worklog, báo cáo cá nhân và các tài liệu hỗ trợ. Nhờ vậy, em có thể nhìn lại toàn bộ quy trình, rút ra bài học và cải thiện cách làm cho những lần thực hiện tiếp theo.

### 2.4.5. Tăng cường kỹ năng trình bày và chia sẻ kiến thức

Ngoài việc triển khai hệ thống, em còn học cách trình bày kết quả của mình bằng văn bản, sơ đồ và hình ảnh minh họa. Việc xây dựng website báo cáo bằng Hugo giúp em hiểu thêm về cách tổ chức nội dung kỹ thuật, cách kết nối các trang với nhau và cách xây dựng một sản phẩm có thể chia sẻ cho người khác xem một cách trực quan.

## 2.5. Kết quả đạt được qua đợt thực tập

Qua đợt thực tập, em đã đạt được nhiều kết quả đáng kể, cả về kiến thức chuyên môn, kỹ năng thực hành, kinh nghiệm làm việc và những đóng góp cụ thể cho dự án. Dưới đây là các kết quả chính mà em đã đạt được.

### 2.5.1. Những nội dung kiến thức lý thuyết đã được củng cố

Trong suốt thời gian thực tập, em có cơ hội củng cố và mở rộng nhiều kiến thức lý thuyết quan trọng, bao gồm:

- Kiến thức về điện toán đám mây và vai trò của AWS trong việc xây dựng các hệ thống hiện đại.
- Kiến thức về Machine Learning, đặc biệt là phân loại dữ liệu bằng mô hình Random Forest và cách đánh giá hiệu quả của mô hình.
- Hiểu rõ hơn về quy trình xây dựng một pipeline ML end-to-end, từ thu thập dữ liệu, tiền xử lý, huấn luyện, triển khai đến dự đoán thời gian thực.
- Kiến thức về kiến trúc hệ thống phân tán, xử lý dữ liệu streaming và cách kết hợp nhiều dịch vụ để tạo thành một giải pháp hoàn chỉnh.
- Kiến thức về bảo mật, phân quyền và quản lý tài nguyên trên nền tảng cloud.

Những kiến thức này giúp em hiểu được rằng một mô hình AI chỉ là một phần của toàn bộ hệ thống. Để mô hình thực sự có giá trị, cần có các thành phần hỗ trợ như lưu trữ dữ liệu, API, luồng xử lý, giám sát hệ thống và cơ chế cảnh báo.

### 2.5.2. Những kỹ năng thực hành đã học hỏi được

Bên cạnh kiến thức lý thuyết, đợt thực tập còn giúp em phát triển nhiều kỹ năng thực hành rất cần thiết trong môi trường công nghệ hiện đại:

- Kỹ năng triển khai và cấu hình các dịch vụ AWS trên môi trường thực tế.
- Kỹ năng viết script và xử lý dữ liệu bằng Python phục vụ cho huấn luyện mô hình và kiểm thử hệ thống.
- Kỹ năng xây dựng kiến trúc hệ thống dựa trên yêu cầu bài toán cụ thể.
- Kỹ năng xây dựng tài liệu kỹ thuật, báo cáo và trình bày nội dung bằng Markdown, sơ đồ và hình ảnh minh họa.
- Kỹ năng kiểm tra lỗi, xử lý sự cố và tối ưu cấu hình hệ thống.
- Kỹ năng làm việc có trách nhiệm với thời gian, tiến độ và chất lượng sản phẩm.

Ngoài ra, em cũng học được cách tiếp cận công việc có tổ chức hơn, biết ưu tiên các nhiệm vụ theo mức độ quan trọng và không ngừng cải thiện chất lượng sản phẩm sau mỗi lần kiểm thử.

### 2.5.3. Những kinh nghiệm thực tiễn đã tích lũy được

Đây là phần mang lại giá trị lớn nhất trong đợt thực tập. Em không chỉ học được cách làm việc với công cụ và công nghệ, mà còn hiểu được những bài học thực tiễn sau:

- Một dự án công nghệ thực tế không thể thành công nếu chỉ tập trung vào một phần nhỏ mà không nhìn tổng thể.
- Việc kiểm thử và đánh giá thường xuyên là điều cần thiết để phát hiện lỗi sớm và tránh ảnh hưởng đến toàn bộ hệ thống.
- Tài liệu hóa quy trình là một bước không thể thiếu, đặc biệt trong các dự án có nhiều thành phần và nhiều bên liên quan.
- Quản lý tài nguyên trên cloud đòi hỏi sự cẩn trọng vì các dịch vụ có thể phát sinh chi phí nếu không được dừng đúng lúc.
- Tư duy tự học là yếu tố quyết định giúp người trẻ thích nghi với môi trường công nghệ thay đổi nhanh chóng.

Những kinh nghiệm này giúp em có cái nhìn thực tế hơn về nghề nghiệp tương lai, đồng thời chuẩn bị tốt cho việc làm việc ở môi trường chuyên nghiệp sau này.

### 2.5.4. Chi tiết các kết quả công việc mà em đã đóng góp cho cơ quan nơi thực tập

Trong đợt thực tập, em đã có những đóng góp đáng kể cho quy trình triển khai và hoàn thiện dự án. Các kết quả công việc cụ thể như sau:

1. Hoàn thiện nội dung về quy trình xây dựng hệ thống phát hiện gian lận giao dịch theo thời gian thực trên AWS.
2. Tìm hiểu và triển khai các thành phần chính của pipeline, từ dữ liệu đầu vào, tiền xử lý, huấn luyện mô hình, triển khai endpoint cho đến dự đoán và gửi cảnh báo.
3. Hỗ trợ xây dựng tài liệu dự án, sơ đồ kiến trúc và nội dung trình bày phục vụ cho mục đích học tập và chia sẻ chuyên môn.
4. Tổng hợp kết quả thực hiện thành các worklog, nội dung blog, phần workshop và báo cáo thực tập, góp phần làm rõ quy trình và kiến thức đã thu được.
5. Tham gia xây dựng website báo cáo bằng Hugo, giúp nội dung trở nên rõ ràng, dễ theo dõi và có thể chia sẻ đến nhiều người đọc.
6. Góp phần vào việc hiểu sâu hơn về cách vận hành một hệ thống AI trên nền tảng cloud, từ khâu xây dựng mô hình cho đến triển khai thực tế và tối ưu tài nguyên sử dụng.

Ngoài ra, em còn có thể nhìn nhận những đóng góp này không chỉ là kết quả của bản thân mà còn là kết quả của quá trình học hỏi, thử nghiệm, sửa đổi và hoàn thiện liên tục. Điều này cho thấy triển khai một dự án công nghệ thực tế đòi hỏi không chỉ kỹ năng chuyên môn mà còn cả sự kiên trì và tinh thần trách nhiệm.

## Kết luận

Qua đợt thực tập tại AWS, em đã có cơ hội tiếp cận với một môi trường học tập và làm việc thực tế, nơi kiến thức lý thuyết được kết nối với ứng dụng thực tế một cách rõ nét. Dự án về hệ thống phát hiện gian lận giao dịch trên AWS đã mang lại cho em những hiểu biết sâu sắc về Machine Learning, Cloud Computing, kiến trúc hệ thống và quy trình triển khai sản phẩm. Bên cạnh những kiến thức chuyên môn, em còn rèn luyện được nhiều kỹ năng mềm như tự học, làm việc nhóm, trình bày và giải quyết vấn đề.

Nhìn chung, đợt thực tập đã giúp em củng cố niềm đam mê với lĩnh vực công nghệ, đặc biệt là Data Science và Cloud Engineering. Em nhận thấy rằng thành công trong môi trường công nghệ không chỉ đến từ khả năng lập trình hay hiểu thuật toán, mà còn từ khả năng kết nối nhiều thành phần, làm việc có hệ thống và luôn sẵn sàng học hỏi. Đây sẽ là nền tảng quan trọng để em tiếp tục phát triển trong tương lai, cả trong học tập lẫn công việc chuyên nghiệp.
