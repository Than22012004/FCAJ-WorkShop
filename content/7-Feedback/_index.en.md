---
title: "Sharing and Feedback"
date: 2026-04-19
weight: 7
chapter: false
pre: " <b> 7. </b> "
---

Throughout my internship and the process of developing this workshop website, I had the opportunity to experience not only cloud technologies but also the complete workflow of documenting and presenting a technical project. Preparing the report in the form of a website required me to organize information logically, explain technical concepts clearly, and ensure that readers could easily understand and reproduce the implementation process.

The project I developed focuses on **credit card fraud detection using Machine Learning on AWS**. It integrates multiple technologies, including data processing, machine learning, cloud computing, real-time data streaming, monitoring, and cost management. More importantly, it allowed me to understand how these individual components work together to form a complete cloud-based solution.

## 1. Experience with the Internship Program

One aspect that impressed me most about the internship program was its emphasis on practical implementation rather than theoretical learning alone. Instead of studying AWS services independently, I was encouraged to combine them into a complete architecture capable of solving a real business problem.

Building the Fraud Detection system required integrating several AWS services, each with a different responsibility within the overall pipeline:

- Amazon S3 for storing datasets, trained models, and prediction results.
- Amazon SageMaker for model training and deployment.
- Amazon API Gateway and AWS Lambda for handling prediction requests.
- Amazon Kinesis for processing streaming transaction data.
- Amazon SNS for fraud notifications.
- Amazon Kinesis Firehose for storing prediction history.
- Amazon CloudWatch for monitoring logs and system performance.

Working with these services helped me understand the importance of designing an end-to-end architecture instead of viewing cloud services as isolated components.

---

## 2. Learning Process

The internship encouraged independent learning and continuous problem solving. Many concepts, such as IAM permissions, SageMaker deployment, real-time inference, and Hugo website generation, were initially unfamiliar to me. Instead of simply following tutorials, I gradually explored documentation, tested different approaches, and documented the knowledge I gained.

Throughout the implementation process, I continuously asked myself questions such as:

- How does data move between different AWS services?
- What is the responsibility of each component?
- Which deployment steps should be demonstrated with screenshots?
- Which AWS resources require cleanup after testing?
- How can the workflow be explained so that another learner can reproduce it?

Answering these questions helped me develop a deeper understanding of the project while improving the overall quality of the report.

---

## 3. Relationship to My Academic Background

This internship closely matches my academic interests in **Data Science**, **Machine Learning**, and **Cloud Engineering**.

Previously, my learning mainly focused on training machine learning models and evaluating prediction accuracy. Through this project, I realized that deploying an ML model into production requires much more than model performance. A practical solution also depends on data storage, deployment infrastructure, APIs, monitoring, security, logging, and operational management.

This broader perspective helped me better understand the complete lifecycle of a machine learning application deployed in a cloud environment.

---

## 4. Achievements

One achievement that I value most is transforming the original workshop template into a project that reflects my own implementation. Rather than simply following the provided content, I redesigned the workshop around the Fraud Detection pipeline and updated many sections to better match the architecture I actually built.

The report is organized into several well-defined sections, including:

- Personal information
- Weekly worklog
- Project proposal
- Technical blog articles
- Event participation
- Workshop implementation
- Self-evaluation
- Feedback and future plans

This structure made it easier to manage progress while presenting the project in a logical and consistent manner.

---

## 5. Challenges

### 5.1 Understanding the Overall Architecture

The Fraud Detection system involves multiple AWS services working together. Initially, understanding how these services communicate with one another was challenging. To simplify the explanation, I separated the architecture into two major phases:

- **Training Pipeline**, covering data preparation, preprocessing, model training, and deployment.
- **Real-Time Inference Pipeline**, covering transaction ingestion, prediction, alerting, and historical storage.

This separation made both the implementation and the report easier to understand.

### 5.2 Building the Workshop Website

Another challenge was learning how Hugo transforms Markdown content into a complete website. During development, I became familiar with Hugo's folder structure, multilingual content organization, image management, and static resource handling.

One mistake I encountered was using local Windows file paths for images instead of Hugo's static resource paths. Correcting this issue improved my understanding of how static assets are served in Hugo websites.

### 5.3 Selecting Supporting Evidence

Choosing appropriate screenshots was also an important part of preparing the report. Instead of documenting every configuration page, I selected screenshots that clearly demonstrate meaningful milestones, such as:

- Amazon S3 bucket structure
- Data Lake organization
- SageMaker Endpoint deployment
- API Gateway configuration
- Lambda functions
- Kinesis Data Streams
- SNS notification emails
- Resource cleanup after deployment

This approach keeps the report concise while still providing sufficient evidence of implementation.

---

## 6. Suggestions

Based on my experience, I would suggest several improvements for future internship programs:

- Provide a clearer reporting guideline with milestones for each required section.
- Include a short tutorial explaining Hugo project organization, especially image management.
- Introduce a brief workshop on building and previewing Hugo websites before submission.
- Encourage students to distinguish between implemented features, conceptual designs, and future work to improve transparency.
- Place greater emphasis on AWS cost management and resource cleanup throughout the project.

---

## 7. Recommendation

I would recommend this internship program to students who are interested in cloud computing, AWS, or machine learning applications.

The program provides valuable opportunities to build a complete personal project while developing practical skills in cloud architecture, documentation, and technical presentation. Although self-learning is required throughout the process, overcoming these challenges contributes significantly to professional growth.

---

## 8. Future Development

In the future, I plan to continue improving the Fraud Detection system by focusing on several areas:

- Expanding end-to-end testing with more transaction scenarios.
- Developing dashboards to monitor prediction results.
- Strengthening IAM policies following the principle of least privilege.
- Enhancing monitoring through CloudWatch metrics and logs.
- Improving documentation and maintaining both Vietnamese and English versions of the workshop website.

---

## 9. Final Reflection

Completing this internship has strengthened both my technical knowledge and my ability to communicate technical solutions effectively. Beyond building a machine learning model, I learned how to design a complete cloud architecture, document implementation procedures, and organize technical knowledge in a way that others can easily understand and reproduce.

The most meaningful lesson I gained is that the success of a cloud solution depends not on the number of AWS services it uses, but on how effectively those services are integrated to address a real-world problem. This project has provided me with valuable experience that will support both my future studies and my professional career.