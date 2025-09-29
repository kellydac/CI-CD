# main.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    # A simple greeting
    return "Hello, World! The CI/CD Pipeline worked! Version 2.1"
