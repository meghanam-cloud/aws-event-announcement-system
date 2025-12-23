import json
import boto3
import os

sns_client = boto3.client("sns")

SNS_TOPIC_ARN = os.environ["SNS_TOPIC_ARN"]

def lambda_handler(event, context):
    body = json.loads(event.get("body", "{}"))

    title = body.get("title", "No Title")
    message = body.get("message", "No message provided")

    full_message = f"📢 {title}\n\n{message}"

    sns_client.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=full_message,
        Subject=f"New Event: {title}"
    )

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "OPTIONS,POST"
        },
        "body": json.dumps({"status": "🎉 Announcement sent successfully!"})
    }
