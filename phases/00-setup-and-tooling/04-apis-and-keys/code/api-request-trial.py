import os
import json
import urllib.request




def api_call_with_demo():
    api_key = os.environ.get("COURSE_DEMO_KEY")
    if not api_key:
        print("Set Demo key first")
        return

    status_messages = {
        200 : "Success",
        400 : "Malformed request", 
        401 : "Missing or invalid key",
        403 : "Insufficient permission",
        429 : "Rate limited",
        500 : "Provider failure",
        502 : "Provider failure",
        503 : "Provider failure"
    }

    for status in status_messages:
        status = 418
        message = status_messages.get(status, "Unexpected status")
    print(f"Status {status}: {message}")


    url = "https://example.invalid/v1/messages"
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01"
    }


    body = json.dumps({
        "model" : "demo-model",
        "max_tokens": 64,
        "messages": [{"role": "user", "content": "What is a neural network in one sentence?"}],
    }).encode()

    req = urllib.request.Request(url, data=body, headers=headers, method="POST")


    print(req.get_method())
    print(req.full_url)
    print(list(req.headers.keys()))
    print(len(req.data))


    mock_response = {
        "content" : [
            {
                "type": "text",
                "text": "learning API done" 
            }
        ],
        "usage": {
            "input_tokens": 10,
            "output_tokens": 20
        }
    }
    response_bytes = json.dumps(mock_response).encode("utf-8")
    parsed_response = json.loads(response_bytes)

    response_text = parsed_response["content"][0]["text"]
    input_tokens = parsed_response["usage"]["input_tokens"]
    output_tokens = parsed_response["usage"]["output_tokens"]

    print(response_text)
    print(f"Tokens: {input_tokens} in, {output_tokens} out")

api_call_with_demo()
    