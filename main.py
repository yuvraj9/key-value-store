import socketio
from flask_restful import Api
from kvstore.resource import *
from kvstore.sockets import sio
from flask import Flask, request

# Creating instance of flask
app = Flask(__name__)

# wrap with a WSGI application
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)


api = Api(app)

# Adding routing for class
api.add_resource(KeyValueStore, "/kv")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
