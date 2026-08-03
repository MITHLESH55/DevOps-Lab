from flask import Flask
import psycopg2
import os
import time

app = Flask(__name__)

# Wait for PostgreSQL to be ready
time.sleep(5)

# Connect to PostgreSQL
conn = psycopg2.connect(
    host=os.getenv("DB_HOST", "db"),
    database=os.getenv("DB_NAME", "flaskdb"),
    user=os.getenv("DB_USER", "admin"),
    password=os.getenv("DB_PASSWORD", "admin123")
)

cur = conn.cursor()

# Create table if it doesn't exist
cur.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id SERIAL PRIMARY KEY,
    text VARCHAR(100)
);
""")
conn.commit()


@app.route("/")
def home():
    # Insert one record
    cur.execute("INSERT INTO messages(text) VALUES (%s);", ("Hello DevOps",))
    conn.commit()

    # Read all records
    cur.execute("SELECT * FROM messages;")
    rows = cur.fetchall()

    return f"Database Records: {rows}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)