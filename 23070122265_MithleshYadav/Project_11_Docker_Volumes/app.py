from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

DATA_DIR = '/app/data'
PERSISTENCE_FILE = os.path.join(DATA_DIR, 'greeting_log.txt')

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

@app.route('/')
def hello_world():
    message = 'Hello, Docker!'
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(PERSISTENCE_FILE, 'a') as f:
        f.write(f"{timestamp}: {message}\n")

    log_content = ""

    try:
        with open(PERSISTENCE_FILE, 'r') as f:
            log_content = f.read()
    except FileNotFoundError:
        log_content = "No previous greetings logged yet."

    return f"{message}<br>Log:<br><pre>{log_content}</pre>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
