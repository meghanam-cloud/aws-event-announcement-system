# Architecture Overview

This project is built using a fully serverless, event-driven architecture on AWS.

## Components

- **Amazon S3**
  - Hosts the static HTML frontend.
  - Users submit event announcements through the web page.

- **Amazon API Gateway**
  - Exposes a POST endpoint for submitting announcements.
  - Forwards requests directly to AWS Lambda.

- **AWS Lambda**
  - Processes incoming requests from API Gateway.
  - Reads the event title and message.
  - Publishes the announcement to an SNS topic.
  - Configuration values are managed using environment variables.

- **Amazon SNS**
  - Acts as the notification layer.
  - Sends email notifications to all subscribed users.

## Flow

1. User opens the frontend hosted on S3.
2. User submits an announcement form.
3. API Gateway receives the HTTP request.
4. Lambda processes the request and publishes to SNS.
5. SNS sends email notifications to subscribers.
