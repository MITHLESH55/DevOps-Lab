from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>DevOps Project 1</h1>
    <h2>Dockerizing Jenkins Pipeline</h2>
    <p>Flask application deployed successfully using Jenkins and Docker.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)