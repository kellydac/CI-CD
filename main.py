# main.py

from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    # This line introduces a bug that will crash the server.
    bad_variable = 1 / 0
    return "This will never be returned."

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
