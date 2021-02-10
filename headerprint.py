from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def headerprint():
    print(request.headers)
    return 'ok'
