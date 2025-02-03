from flask import Flask, request, jsonify
from threading import Thread
import tkinter as tk
from tkinter import ttk, messagebox
import requests

proxies = {
    "http": "http://127.0.0.1:8081",
    "https": "http://127.0.0.1:8081",
}

# Flask server setup
def start_dummy_server(shared_data):
    app = Flask(__name__)

    @app.route("/test", methods=["POST"])
    def test_endpoint():
        body = request.json
        response_text = shared_data.get("ai_text", "")
        return jsonify({"received": body, "response": response_text})

    app.run(port=5001, debug=False, threaded=True)

# Request handler for Tkinter GUI
def make_request():
    url = "http://127.0.0.1:5001/test"
    body = body_text.get("1.0", tk.END).strip()

    try:
        response_proxy = requests.post(url, json=body, proxies=proxies) if proxies else requests.post(url, json=body)
        
        response_text.delete("1.0", tk.END)
        response_text.insert(tk.END, response_proxy.text)
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Request Failed", str(e))

# Tkinter GUI setup
root = tk.Tk()
root.title("AI Guard")
root.geometry("600x600")
root.configure(bg="#f0f0f0")

# Shared data dictionary for inter-thread communication
shared_data = {"ai_text": ""}

ai_frame = tk.Frame(root, bg="#f0f0f0", padx=10, pady=10, bd=2, relief="solid")
ai_frame.pack(fill="x", padx=10, pady=5)

ai_title_label = tk.Label(ai_frame, text="Target AI agent", bg="#f0f0f0", font=("Arial", 12, "bold"))
ai_title_label.pack(anchor="w") 

ai_label = tk.Label(ai_frame, text="Dummy Output", bg="#f0f0f0")
ai_label.pack()
ai_text = tk.Text(ai_frame, height=5, width=50)
ai_text.pack()

input_output_frame = tk.Frame(root, bg="#f0f0f0", padx=10, pady=10, bd=2, relief="solid")
input_output_frame.pack(fill="both", expand=True, padx=10, pady=5)

io_title_label = tk.Label(input_output_frame, text="Communication", bg="#f0f0f0", font=("Arial", 12, "bold"))
io_title_label.pack(anchor="w") 

send_button = tk.Button(input_output_frame, text="Send Request", command=make_request, bg="#007BFF", fg="white")
send_button.pack(pady=5)

input_frame = tk.Frame(input_output_frame, bg="#f0f0f0", padx=10, pady=10)
input_frame.pack(expand=True)

body_label = tk.Label(input_frame, text="Input from employee", bg="#f0f0f0")
body_label.pack()
body_text = tk.Text(input_frame, height=5, width=50)
body_text.pack()

output_frame = tk.Frame(input_output_frame, bg="#f0f0f0", padx=10, pady=10)
output_frame.pack(expand=True)

response_label = tk.Label(output_frame, text="Ouput from Target AI agent", bg="#f0f0f0")
response_label.pack()
response_text = tk.Text(output_frame, height=10, width=50)
response_text.pack()

# Update shared data when the Tkinter Text widget content changes
def update_shared_data():
    shared_data["ai_text"] = ai_text.get("1.0", tk.END).strip()

# Tkinter event to update shared data on any text changes
ai_text.bind("<KeyRelease>", lambda event: update_shared_data())

# Start the dummy server in a separate thread
server_thread = Thread(target=start_dummy_server, args=(shared_data,), daemon=True)
server_thread.start()

# Start the Tkinter main loop
root.mainloop()
