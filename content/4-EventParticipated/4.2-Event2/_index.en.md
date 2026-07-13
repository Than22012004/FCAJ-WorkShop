---
title: "Event 2 - AWS Security and Certification"
date: 2026-06-15
weight: 2
chapter: false
pre: " <b> 4.2. </b> "
---

## 1. Event Information

- **Event:** AWS Security & Certification Workshop
- **Date:** Saturday, 15 June
- **Venue:** AWS Vietnam Office
- **Role:** Participant

## 2. Evidence of Participation

![Proof of participation in Event 2](https://than22012004.github.io/FCAJ-WorkShop/images/event_2.jpg)

## 3. Event Overview

This event focused on critical topics for running production systems in the cloud, including security, service level guarantees, and career development through AWS certifications.

### 09:00 - 10:00 AM: AWS Security Agent

The opening session introduced the **AWS Security Agent** and comprehensive approaches to cloud security. The speaker demonstrated how security agents can automatically monitor environments, detect potential threats, and respond in real-time. The content also dived into setting up Guardrails, the principle of least privilege, and integrating security processes (DevSecOps) into the software development lifecycle without slowing down deployments.

### 10:00 - 10:45 AM: Introduction to SLA (Service Level Agreement)

The second session focused on **SLA (Service Level Agreement)**. Participants learned how to read and analyze AWS SLA documents for specific services (like Amazon S3, EC2, API Gateway). The speaker explained concepts such as Uptime, RTO (Recovery Time Objective), RPO (Recovery Point Objective), and how to architect systems to meet high SLA tiers (such as 99.99% or 99.999%) using Multi-AZ and Multi-Region deployments.

### 10:45 - 11:00 AM: Break

Networking and discussion with security experts.

### 11:00 - 12:00 PM: Guide to Taking AWS Certification Exams

The final session provided practical guidance for individuals starting their cloud journey. The speaker shared the roadmap for earning AWS certifications (from Cloud Practitioner and Associate to Professional and Specialty). Topics included how to register for exams, official and free study resources (like AWS Skill Builder), test-taking strategies, and the importance of gaining hands-on experience by building actual projects (like a Data Lake or Fraud Detection system).

## 4. Reflection and Learning Outcomes

Attending the second event provided me with a more comprehensive and practical perspective on designing systems that are not only functional but also secure and highly available.

The knowledge about **AWS Security Agent** emphasized the importance of system security. In my fraud detection project, managing access permissions via IAM Roles for services (Lambda, API Gateway, SageMaker) must be carefully configured following the least privilege principle, while monitoring CloudWatch logs acts as an essential security observation layer.

The introduction to **SLA** improved my architectural thinking. When designing a real-time pipeline with Kinesis and SageMaker, I must consider what Uptime these services guarantee and how my system should gracefully handle situations if a component temporarily fails.

Finally, the session on **AWS certifications** gave me clear motivation and a learning roadmap. It validated that hands-on projects, like the Real-time ML on AWS system I am building, are the best stepping stones to deeply understand cloud services and will greatly support my goal of achieving recognized AWS certifications in the future.
