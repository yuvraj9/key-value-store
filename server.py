import datetime
import sys
import os
import json
from flask import Flask, request
from waitress import serve
from werkzeug.exceptions import ExpectationFailed
import socketio
import logging

# create a Socket.IO server
sio = socketio.Server(logger=True, async_mode='threading')
app = Flask(__name__)
# wrap with a WSGI application
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)
# app.config['SECRET_KEY'] = 'secret!'
# thread = None

if not os.path.exists("store.json"):
    file = open('store.json', 'x')
    with open('store.json', 'w') as file:
        json.dump("{}", file)


with open('store.json', 'r') as file:  
    data = file.read() 

kvStore = json.loads(data)

def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s", "%Y-%m-%d %H:%M:%S")
    logHandler = logging.StreamHandler(sys.stdout)
    logHandler.setLevel(logging.INFO)
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)

    return logger

logger = get_logger()

class keyvalue:

    def __init__(self) -> None:
        print("Starting Flask server")
        
    def get_value(self, key):
        self.key = key
        try:
            value = kvStore.get(key)
            if not value:
                return "Key Doesn't exist"
            return value
        except Exception as error:
            logger.error("Error: %s" % str(error))

    def set_value(self, key, value):
        self.key = key
        self.value = value

        newKeyValue = {
            key: value,
        }
        time = str(datetime.datetime.now())

        kvStore.update(newKeyValue)

        updates = "Updated key: {} and value: {}".format(key,value)
        logger.info(updates)

        key_update_event(updates)

        with open('store.json', 'w') as file: 
            json.dump(kvStore, file)
        
        return "Done"

### Defining socket Events. These help in sending events to clients.
### 
@sio.event
def key_update_event(data):
    sio.emit('key_update', {'data': data})

@sio.event
def connect(sid, environ):
    sio.emit('connected', {'data': 'Connected', 'count': 0}, room=sid)

@sio.event
def disconnect(sid):
    print('Client disconnected')

# Calling keyvalue class
kv = keyvalue()

#  curl --header "Content-Type: application/json" --request GET --data '{"key": "key"}' http://localhost:5000/kv
@app.route("/kv", methods=["GET"])
def get():
    parameters = request.json
    key = parameters['key']
    return kv.get_value(key)

#  curl --header "Content-Type: application/json" --request PUT --data '{"key": "name", "value": "yuvraj"}' http://localhost:5000/kv
@app.route("/kv", methods=["PUT"])
def update():
    parameters = request.json
    key = parameters['key']
    value = parameters['value']
    return kv.set_value(key, value)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)