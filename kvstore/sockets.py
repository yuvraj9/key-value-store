import socketio
from utils import get_logger

logger = get_logger()

# create a Socket.IO server
sio = socketio.Server(logger=True, async_mode='threading')


@sio.event
def key_update_event(data):
    """
    Broadcasts the event message to all clients.

    Parameter:
        data: Data to send to clients.
    """
    try:
        sio.emit('key_update', {'data': data})
    except Exception as error:
        logger.error("Error while broadcasting {err}".format(err=error))


@sio.event
def connect(sid, test):
    """
    The function to establish a connection.
    """
    try:
        sio.emit('connected', {'data': 'Connected', 'count': 0}, room=sid)
    except socketio.exceptions.ConnectionError as error:
        logger.error("Connection Error {err}".format(err=error))


@sio.event
def disconnect(sid):
    """
    The function is called when a client disconnects
    """

    print('Client disconnected')
