from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def hello():
    print request.remote_addr
    return "Hello World!"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
