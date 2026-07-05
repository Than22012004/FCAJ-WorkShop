---
title: "Self Evaluation"
date: 2026-04-19
weight: 6
chapter: false
pre: " <b> 6. </b> "
---

During my internship at **AWS** as a **Cloud Engineering Intern**, I completed an individual project titled **Credit Card Fraud Detection System using Machine Learning on AWS**.

The objective of this project was to design and implement an end-to-end Machine Learning pipeline, covering both model training and real-time inference on AWS. The architecture consists of two main areas:

- **Training Zone**: stores datasets in Amazon S3, trains a Random Forest model using Amazon SageMaker, generates model artifacts, and deploys a SageMaker Endpoint.
- **Real-time Zone**: receives transaction requests through Amazon API Gateway, processes data with AWS Lambda, streams data via Amazon Kinesis, performs predictions using the SageMaker Endpoint, sends fraud alerts through Amazon SNS, and stores prediction results in Amazon S3 using Kinesis Firehose.

Through this project, I was able to apply my knowledge of Machine Learning while gaining hands-on experience in designing, deploying, and operating cloud-based AI solutions using AWS services.

The main tasks completed during the project include:

- Analyzing the credit card fraud detection problem and identifying system requirements.
- Designing a cloud architecture consisting of Training Zone and Real-time Zone.
- Building a Data Lake on Amazon S3 to store datasets, model artifacts, and prediction results.
- Training a Random Forest model using Amazon SageMaker and deploying it as a real-time inference endpoint.
- Developing a real-time transaction processing pipeline using Amazon API Gateway, AWS Lambda, Amazon Kinesis, and SageMaker Endpoint.
- Configuring Amazon SNS to send notifications when fraudulent transactions are detected.
- Delivering prediction results to Amazon S3 through Amazon Kinesis Firehose.
- Developing a Hugo Workshop Website that includes Proposal, Worklog, Workshop, Blog, Events, Self Evaluation, and Feedback sections.
- Performing system testing, validating deployment results, and documenting resource cleanup procedures to optimize AWS costs.

Throughout the internship, I evaluated my performance based on the following criteria:

| No. | Evaluation Criteria | Rating | Comments |
| --- | --- | --- | --- |
| 1 | **Technical Knowledge** | Good | I successfully applied Machine Learning, Python, and AWS services to build a complete fraud detection system from model training to real-time inference. |
| 2 | **Learning Ability** | Good | I proactively learned and applied AWS services such as Amazon S3, SageMaker, API Gateway, Lambda, Kinesis, SNS, and Firehose, while understanding how they work together in a cloud-based ML system. |
| 3 | **Proactiveness** | Good | I independently designed the system architecture and implemented the processing pipeline instead of relying solely on available templates or tutorials. |
| 4 | **Responsibility** | Good | I completed all major project components, including implementation, testing, optimization, documentation, and deployment guidance. |
| 5 | **Work Discipline** | Fairly Good | I consistently monitored project progress and reviewed each deployment step. However, I need to improve my time management to complete future projects more efficiently. |
| 6 | **Communication and Presentation** | Good | I organized the report in a clear and structured manner, supported by architecture diagrams and AWS Console screenshots to explain the implementation process. |
| 7 | **Collaboration and Communication** | Fairly Good | I accepted feedback from my supervisor and continuously improved both the system architecture and documentation. I also recognize the need to communicate technical issues earlier when facing complex challenges. |
| 8 | **Problem-Solving Skills** | Good | I divided the project into independent modules such as model training, deployment, streaming, alerting, and storage, making development and troubleshooting more manageable. |
| 9 | **Tool Proficiency** | Good | I gained practical experience using AWS Console, Hugo, Markdown, and Git to develop the project and manage technical documentation. |
| 10 | **Contribution to the Project** | Good | I successfully developed a complete fraud detection solution including model training, deployment, real-time prediction, alerting, and data storage, together with comprehensive deployment documentation. |
| 11 | **Self-Improvement** | Good | I continuously reviewed the system architecture, refined the documentation, added implementation evidence, and improved deployment procedures throughout the project. |
| 12 | **Overall Performance** | Good | Overall, I achieved the project's objectives and gained a solid understanding of deploying Machine Learning solutions on AWS from data preparation to real-time production inference. |

## Strengths

- Developed a solid understanding of designing and deploying Machine Learning systems on AWS.
- Successfully designed a cloud architecture consisting of Training Zone and Real-time Zone.
- Gained hands-on experience with Amazon S3, SageMaker, API Gateway, Lambda, Kinesis, SNS, and Firehose.
- Learned how to deploy Machine Learning models as SageMaker Real-time Endpoints.
- Understood how to integrate multiple AWS services into a streaming data pipeline.
- Improved technical documentation skills by developing a Hugo-based workshop website.

## Areas for Improvement

- Gain deeper knowledge of system optimization and scalability for high-volume transaction processing.
- Improve cost optimization strategies, particularly for SageMaker Endpoints and real-time AWS services.
- Perform more comprehensive testing with larger datasets to evaluate system reliability.
- Learn advanced monitoring, logging, and security techniques for production Machine Learning systems.

## Future Development Plan

In the next stage, I plan to focus on the following improvements:

1. Evaluate additional Machine Learning and Deep Learning algorithms to improve prediction accuracy.
2. Implement an automated MLOps pipeline for model retraining and deployment.
3. Develop monitoring dashboards for prediction results and system performance.
4. Learn CI/CD and Infrastructure as Code (IaC) to automate AWS deployment.
5. Continue improving my technical English skills to better understand AWS documentation and emerging cloud technologies.

## Self-Evaluation Summary

This internship provided valuable experience in combining Machine Learning techniques with AWS Cloud services to develop a practical credit card fraud detection system. The project helped me understand that deploying Machine Learning models in production involves much more than model training. It also requires careful consideration of data management, endpoint deployment, real-time processing, monitoring, alerting, security, resource management, and operational costs.

Overall, I evaluate my internship performance as **Good**. The project strengthened both my technical knowledge and practical cloud engineering skills, providing a solid foundation for pursuing future work in Cloud Computing, Machine Learning Engineering, and MLOps.