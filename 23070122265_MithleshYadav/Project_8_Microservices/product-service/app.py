from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "Product Service",
        "status": "running",
        "products": [
            {"id": 1, "name": "Laptop", "price": 75000},
            {"id": 2, "name": "Smartphone", "price": 35000},
            {"id": 3, "name": "Headphones", "price": 5000}
        ]
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
