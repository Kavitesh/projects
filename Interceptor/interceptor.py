from mitmproxy import http
import datetime

# Log file to store request and response details
LOG_FILE = "http_traffic.log"

# Function to log data
def log_message(message: str):
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - {message}\n")

# Log outgoing requests
def request(flow: http.HTTPFlow) -> None:
    request_details = (
        f"REQUEST:\n"
        f"URL: {flow.request.pretty_url}\n"
        f"Method: {flow.request.method}\n"
        f"Headers: {dict(flow.request.headers)}\n"
        f"Body: {flow.request.text}\n"
        "-----------------------\n"
    )
    log_message(request_details)
    # Example: Add a custom header
    if "example.com" in flow.request.pretty_url:
        flow.request.headers["Custom-Header"] = "ModifiedValue"
        log_message(f"Modified request to {flow.request.pretty_url}")

# Log incoming responses
def response(flow: http.HTTPFlow) -> None:
    response_details = (
        f"RESPONSE:\n"
        f"URL: {flow.request.pretty_url}\n"
        f"Status Code: {flow.response.status_code}\n"
        f"Headers: {dict(flow.response.headers)}\n"
        f"Body: {flow.response.text}\n"
        "=======================\n"
    )
    log_message(response_details)
    if "example.com" in flow.request.pretty_url:
        # Example: Replace a value in the response body
        flow.response.text = flow.response.text.replace("old_value", "new_value")
        log_message(f"Modified response from {flow.request.pretty_url}")
