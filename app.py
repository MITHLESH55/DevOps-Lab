from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    print("User Authentication Feature Added")
    return "Hello World from Flask - User Authentication Feature"

if __name__ == "__main__":
    app.run(debug=True)