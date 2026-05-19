import json
import boto3
import os

AWS_ENDPOINT = os.environ.get("AWS_ENDPOINT")
INSTANCE_ID = os.environ.get("INSTANCE_ID")

ec2 = boto3.client(
    "ec2",
    endpoint_url=AWS_ENDPOINT,
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1"
)

def lambda_handler(event, context):

    body = json.loads(event.get("body", "{}"))
    action = body.get("action")

    if action == "start":

        ec2.start_instances(InstanceIds=[INSTANCE_ID])

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Instance started",
                "instance_id": INSTANCE_ID
            })
        }

    elif action == "stop":

        ec2.stop_instances(InstanceIds=[INSTANCE_ID])

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Instance stopped",
                "instance_id": INSTANCE_ID
            })
        }

    else:

        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "Invalid action"
            })
        }
