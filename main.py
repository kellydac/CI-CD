# main.py

from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World! The CI/CD Pipeline worked! Version 2.0"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
