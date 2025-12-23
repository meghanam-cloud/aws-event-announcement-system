# AWS Event Announcement System

This project is a serverless event announcement system built using AWS services.
A static frontend hosted on Amazon S3 allows users to submit announcements, which are processed by API Gateway and AWS Lambda.
The Lambda function publishes the announcement to an SNS topic, and SNS sends email notifications to subscribed users.

## Architecture Overview

The application follows a fully serverless, event-driven architecture.

**Flow:**
1. The user opens a static web page hosted on Amazon S3.
2. The user submits an event announcement using the form.
3. Amazon API Gateway receives the HTTP POST request.
4. AWS Lambda processes the request and publishes the message to an SNS topic.
5. Amazon SNS sends email notifications to all subscribed users.

## AWS Services Used

- **Amazon S3** – Hosts the static frontend (HTML/CSS/JavaScript)
- **Amazon API Gateway** – Exposes the backend HTTP endpoint
- **AWS Lambda** – Handles request processing and business logic
- **Amazon SNS** – Sends email notifications
- **Amazon CloudWatch** – Logs Lambda execution

## Configuration Notes

- Sensitive values such as the SNS Topic ARN are configured using **Lambda environment variables**.
- Real AWS endpoints and account-specific details are not committed to this repository for security reasons.

## Proof of Execution

Screenshots demonstrating:
- The working frontend UI
- Successful submission response
- Email notification received from Amazon SNS  

are available in the `screenshots/` directory.
