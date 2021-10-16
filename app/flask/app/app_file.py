from flask import Flask

import socket

from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/')

def hello():
    with open('hostname.txt', 'r') as file:
        hostname = file.read().replace('\n', '')
    return f"Hello from ContainerID: {socket.gethostname()} on Server {hostname} "


