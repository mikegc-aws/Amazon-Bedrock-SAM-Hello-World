import json
import boto3, botocore

client = boto3.client('bedrock-runtime', 'us-west-2')

def lambda_handler(event, context):

    prompt = "Hello world!"

    kwargs = {
        "modelId": "anthropic.claude-instant-v1",
        "contentType": "application/json",
        "accept": "*/*",
        "body": json.dumps(
            {
                "prompt": "Human: " + prompt + "\\nAssistant:",
                "max_tokens_to_sample": 300, 
                "temperature": 1,
                "top_k": 250,
                "top_p": 0.999,
                "stop_sequences": ["\\n\\nHuman:"],
                "anthropic_version" : "bedrock-2023-05-31"
            }
        )
    }

    resp = client.invoke_model(**kwargs)
    resp_data = json.loads(resp.get('body').read())

    return {
        "statusCode": 200,
        "body": json.dumps(resp_data),
    }
