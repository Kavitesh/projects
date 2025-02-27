import json
import random
import requests
import threading
import time
from flask import Flask, render_template, request

app = Flask(__name__)

AI_PIPELINES = {
 #   "churn": "http://localhost:5001/get_chart_data",
    "recommend": "http://localhost:5002/chart_data",
 #   "popular": "http://localhost:5002/get_chart_data",
 #   "anomaly": "http://localhost:5004/get_chart_data",
}

LOG_ENDPOINTS = {
  #  "churn": "http://localhost:5001/receive_log",
    "recommend": "http://localhost:5002/logs",
  #  "popular": "http://localhost:5002/receive_log",
  #  "anomaly": "http://localhost:5004/receive_log",
}


# Store the latest data for visualization
latest_data = {"churn": {}, "recommend": {}, "grouping": {}, "anomaly": {}}

def fetch_data():
    """Continuously fetch data from all AI pipelines."""
    while True:
        for key, url in AI_PIPELINES.items():
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    latest_data[key] = response.json()
            except Exception as e:
                print(f"Error fetching {key}: {e}")
        time.sleep(5)  # Update every 5 seconds

# Start background data fetching
threading.Thread(target=fetch_data, daemon=True).start()

@app.route("/")
def index():
    return render_template("dashboard.html")

@app.route("/send_log", methods=["POST"])
def send_log():
    """Send logs to all AI pipelines."""
    data = request.json
    for url in LOG_ENDPOINTS.values():
        requests.post(url, json=data)
    return {"message": "Log sent"}

@app.route("/get_data")
def get_data():
    """Send latest AI data to frontend."""
    print(latest_data)
    return latest_data

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
