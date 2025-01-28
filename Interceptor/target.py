import requests

proxies = {
    "http": "http://127.0.0.1:8081",
    "https": "http://127.0.0.1:8081",
}

try:
    response = requests.get("http://example.com", proxies=proxies)
    print(response.text)
except requests.exceptions.ProxyError as e:
    print("ProxyError:", e)
except requests.exceptions.SSLError as e:
    print("SSLError:", e)
except requests.exceptions.RequestException as e:
    print("RequestException:", e)
