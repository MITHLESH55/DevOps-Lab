from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "User Service",
        "status": "running",
        "users": [
            {"id": 1, "name": "Admin User"},
            {"id": 2, "name": "Demo User"}
        ]
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
