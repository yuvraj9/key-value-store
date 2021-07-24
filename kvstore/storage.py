import os
import sys
import json
from utils import get_logger

logger = get_logger()


class Storage():
    """
    This is a class manages the storage of key value store.

    It contains two methods read() and write(). We use these methods
    to read and write in a file.
    """

    def __init__(self):
        """
        Check if file exists. If doesn't exist then it creates a new file.
        After creating new file it writes a empty json in the file.
        """
        try:
            if not os.path.exists("store.json"):
                file = open('store.json', 'x')
                with open('store.json', 'w') as file:
                    json.dump({}, file)
        except Exception as error:
            logger.error("Unexpected error:", error)
            raise Exception("Unable to initialize Storage")

    def read(self):
        """
        The function is used to create[if doesn't exist]/read the file.
        Then we store the data in a variable and return it.

        Returns:
            KVSTORE: Data from the file. If new file we return empty json.
        """
        try:
            # Reads the file
            with open('store.json', 'r') as file:
                data = file.read()

            # Converts file data into a json
            KVSTORE = json.loads(data)

            return KVSTORE

        except Exception as error:
            logger.error("Unexpected error:", error)
            raise Exception("Unable to read Storage")

    def write(self, data):
        """
        The function is used to write data in file.

        Parameters:
            data: Data to write in file.
        """
        try:
            with open('store.json', 'w') as file:
                json.dump(data, file)
        except Exception as error:
            logger.error("Unexpected error:", error)
            raise Exception("Unable to write in Storage")
