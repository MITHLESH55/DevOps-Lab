from flask import Flask, jsonify
import os
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "API Gateway",
        "status": "running",
        "microservices": [
            "User Service",
            "Product Service",
            "Order Service"
        ]
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/config")
def config():
    return jsonify({
        "environment": os.getenv("ENVIRONMENT", "development"),
        "application": os.getenv("APP_NAME", "microservices-app")
    })

@app.route("/services")
def services():
    results = {}

    services = {
        "user_service": os.getenv("USER_SERVICE_URL", "http://user-service:5001"),
        "product_service": os.getenv("PRODUCT_SERVICE_URL", "http://product-service:5002"),
        "order_service": os.getenv("ORDER_SERVICE_URL", "http://order-service:5003")
    }

    for name, url in services.items():
        try:
            response = requests.get(url, timeout=5)
            results[name] = {
                "status": "connected",
                "response": response.json()
            }
        except Exception as e:
            results[name] = {
                "status": "unavailable",
                "error": str(e)
            }

    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
