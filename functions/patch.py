import json


def handler(event, context):

    body = {
        "message": "patch",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response