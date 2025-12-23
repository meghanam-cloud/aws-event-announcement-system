# AWS Event Announcement System

This project is a serverless event announcement system built using AWS services.
A static frontend hosted on Amazon S3 allows users to submit announcements, which are processed by API Gateway and AWS Lambda.
The Lambda function publishes the announcement to an SNS topic, and SNS sends email notifications to subscribed users.
