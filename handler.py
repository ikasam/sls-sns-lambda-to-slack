import json
import urllib3
import os

http = urllib3.PoolManager()


def invoke(event, context):
    message = event['message']
    payload = json.dumps({'text': message})
    url = os.environ["WEBHOOK_URL"]
    resp = http.request('POST', url, body=payload)
    print({
        "url": url,
        "payload": payload,
        "status_code": resp.status,
        "response": resp.data
    })

    return payload
