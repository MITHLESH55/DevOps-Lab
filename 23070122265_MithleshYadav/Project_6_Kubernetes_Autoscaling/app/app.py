from flask import Flask, jsonify
import time

app = Flask(__name__)

posts = [
    {
        "id": 1,
        "username": "mithlesh",
        "content": "Welcome to our Social Media Platform!"
    },
    {
        "id": 2,
        "username": "developer",
        "content": "Running on Kubernetes with autoscaling."
    }
]


@app.route("/")
def home():
    return "Social Media Application is Running!"


@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "social-media-app"
    })


@app.route("/api/posts")
def get_posts():
    return jsonify(posts)

@app.route("/api/load")
def cpu_load():
    start = time.time()
    while time.time() - start < 10:
        for _ in range(100000):
            _ = 12345 * 67890
    return jsonify({
        "status": "completed",
        "message": "CPU load generated for 10 seconds"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)