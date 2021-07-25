#!/usr/bin/env python3

import os
import click
import requests
from click.decorators import argument

URL = os.getenv("URL", "http://localhost:5000")


def get_value(key):
    """
    This function is used to get key value from server.

    Parameters:
        key: The key for which we need to get value.

    Returns:
        response: Returns the value of key from key-value store
    """

    url = URL + '/kv'
    query_params = {
        'key': key
    }

    try:
        response = requests.get(url, json=query_params)
        return response.text
    except requests.exceptions.RequestException as error:
        raise SystemExit(error)


def put_value(key, value):
    """
    This function is used to update key with value in key value store.

    Parameters:
        key: The key for which we need to update value.
        value: The value of key.

    Returns:
        response: Returns the updated key value pair.
    """

    url = URL + '/kv'
    query_params = {
        'key': key,
        'value': value
    }
    try:
        response = requests.put(url, json=query_params)
        return response.text
    except requests.exceptions.RequestException as error:
        raise SystemExit(error)


# Click is being used to create a CLI.
@click.group()
def commands():
    pass


@click.command()
@click.argument(
    'key'
)
def get(key):
    """
    It can be used to get value of a particular key.
    Example -> kv get exampleKey
    """

    response = get_value(key)
    click.echo(response)


@click.command()
@click.argument('key')
@click.argument('value')
def put(key, value):
    """
    It can be used to set key with value.
    Example -> kv get exampleKey exampleValue
    """

    response = put_value(key, value)
    click.echo(response)


# Adding sub commands in kv command.
commands.add_command(get)
commands.add_command(put)


if __name__ == '__main__':
    commands()
