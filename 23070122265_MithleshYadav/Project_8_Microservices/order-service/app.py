from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "Order Service",
        "status": "running",
        "orders": [
            {"id": 101, "user_id": 1, "product_id": 1, "status": "confirmed"},
            {"id": 102, "user_id": 2, "product_id": 3, "status": "processing"}
        ]
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
