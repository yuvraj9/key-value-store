from utils import get_logger
from kvstore.storage import Storage
from flask_restful import Resource, reqparse
from kvstore.sockets import key_update_event

logger = get_logger()


class KeyValueStore(Resource):
    """
    This is a class which returns the values and update keys

    It contains two methods get() and put(). The get() method is used
    to get values for a given key. The put() method is used to update
    the key with value.
    """

    STORAGE = Storage()

    def __init__(self) -> None:
        """
        The constructor for KeyValueStore class.
        """

        self.req_args = reqparse.RequestParser()
        self.req_args.add_argument('key', type=str, required=True)
        self.req_args.add_argument('value', type=str)

    def get(self):
        """
        The function to get value of given key.

        Parameters:
            key : The key for which we need to find the value.

        Returns:
            value: A value for the given key.
        """

        args = self.req_args.parse_args()
        key = args["key"]

        try:
            # Reads the file and get the dictionary which has key-value pairs.
            KVSTORE = self.STORAGE.read()

            # Check for given key in the object and fetches value
            value = KVSTORE.get(key)

            if not value:
                # If key doesn't exist we return error message with a 404
                # status code
                return {'status_code': 404, 'error': "Key Doesn't exist"}, 404

            return {"value": value}

        except Exception as error:
            logger.error("Error: {error}".format(error=str(error)))
            error_message = {"message": str(error), "status_code": 500}
            return error_message, 500

    def put(self):
        """
        The function to update key with value.

        Parameters:
            key : The provided key.
            value: The value to associate with the given key.

        Returns:
            key-value pair: It return the updated the key-value pair in
            json format.
        """

        args = self.req_args.parse_args()
        key = args["key"]
        value = args["value"]
        newKeyValue = {
            key: value,
        }

        try:
            # Reads the file and get the dictionary which has key-value pairs.
            KVSTORE = self.STORAGE.read()

            # Updates the existing object with key value pair.
            KVSTORE.update(newKeyValue)

            updates = "Key: {} set with value: {}".format(key, value)

            # Writes the updated value in file.
            self.STORAGE.write(KVSTORE)

            # Sends a socket broadcast event. All connected clients will
            # recieve this.
            key_update_event(updates)

            return newKeyValue

        except Exception as error:
            logger.error("Error: {error}".format(error=str(error)))
            error_message = {"message": str(error), "status_code": 500}
            return error_message, 500
