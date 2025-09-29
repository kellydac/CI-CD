# main.py

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World! The CI/CD Pipeline worked! Version 2.0"

# (no need for __main__ block when using gunicorn)
