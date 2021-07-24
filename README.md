# Key Value Store
A simple KV (key-value) store web service with a subscription feature. As a user, you can perform put(key, val) and get(key) operations over HTTP and also subscribe to changes happening to any of the keys. It supports a CLI client which consumes the web service supporting following commands a. get <key>: displays the value of an existing key b. put <key> <value>: sets the value of the given key.

## Prerequisites
To easily use it you should have docker installed on your machine to run the webserver. 

## Usage
#### 1. Start webserver using docker
This will start the webserver on your local machine. It will expose the service at 5000 port. 
```
docker run -d -p 5000:5000 ghcr.io/yuvraj9/key-value-store-main:latest
```

#### 2. Download CLI client
To use the CLI client you can use the same the container which is running and execute inside it or you can use it on your local machine.
- *Use CLI in already running docker container*

```

```

### 3. Run commands to perform actions
The CLI client have have three sub commands - get, put and watch.

- *get* -> This will display the value of an existing key.
```
./kv get <key>
```

- *put* -> This sets the value of the given key.
```
./kv put <key> <value>
```

- *watch* -> This displays the changes to Key Value as they happen in real-time.
```
./kv watch
```