from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# To avoid CORS issue
@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)