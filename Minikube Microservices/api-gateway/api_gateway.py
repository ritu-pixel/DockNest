from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def gateway():
    response = requests.get("http://backend-service:5000")
    return f"API Gateway received response: {response.text}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
