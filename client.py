#!/usr/bin/env python3
import click
from click.decorators import argument
import requests
import socketio

sio = socketio.Client()

def get_value(key):
    url = 'http://localhost:5000/kv'

    query_params = {
        'key': key
    }

    response = requests.get(url, json = query_params)

    return response.text

def put_value(key, value):
    url = 'http://localhost:5000/kv'
    query_params = {
        'key': key,
        'value': value
    }
    response = requests.put(url, json = query_params)
    return response.text

@click.group()
def commands():
  pass

@click.command()
@click.argument(
    'key'
)
def get(key):
    """
    It can be used to get value of a particular key. Example -> kv get hello
    """
    response = get_value(key)
    click.echo(response)

@click.command()
@click.argument('key')
@click.argument('value')
def put(key, value):
    """
    It can be used to set value of a particular key. Example -> kv get hello hi
    """
    response = put_value(key, value)
    click.echo(response)

        
@click.command()
def watch():
    sio.connect('http://localhost:5000')
    sio.wait()



commands.add_command(get)
commands.add_command(put)
commands.add_command(watch)



##Sockets
@sio.event
def connect():
    print('connected to server')


@sio.event
def disconnect():
    print('disconnected from server')


@sio.on('key_update')
def my_broadcast_event(data):
    print(data)


if __name__ == '__main__':
    commands()
