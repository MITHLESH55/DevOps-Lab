from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    print("User Authentication Feature Added")
    return "Hello World from Main Branch with User Authentication"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)