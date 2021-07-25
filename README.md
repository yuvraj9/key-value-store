# Key Value Store
A simple KV (key-value) store web service with a subscription feature. As a user, you can perform put(key, val) and get(key) operations over HTTP and also subscribe to changes happening to any of the keys. It supports a CLI client which consumes the web service supporting following commands a. get <key>: displays the value of an existing key b. put <key> <value>: sets the value of the given key.

## 📜 Prerequisites
To easily use it you should have docker installed on your machine to run the webserver. 

---

## 🚀 Usage
### 1. Start webserver using docker
This will start the webserver on your local machine. It will expose the service at 5000 port. 
```
docker run -d -p 5000:5000 ghcr.io/yuvraj9/key-value-store-main:latest
```

### 2. Use CLI client
To use the CLI client you can use the same the container which is running and execute inside it or you can use it on your local machine.
- **Use CLI in already running docker container[Command line is already present as binary executable]**

```
container_id=$(docker ps | grep "ghcr.io/yuvraj9/key-value-store-main" | awk '{print $1}' | head -n 1)
docker exec -it $container_id /bin/sh
kv --help
```

### 3. Run commands to perform actions
The CLI client have have three sub commands - get, put and watch. You can also use ```kv --help```

- **get** -> This will display the value of an existing key.
```
kv get <key>
```

- **put** -> This sets the value of the given key.
```
kv put <key> <value>
```

- **watch** -> This displays the changes to Key Value as they happen in real-time.
```
kv watch
```

---

## 📄 Code Structure
```
key-value-store
├── kvstore
│   └── resource.py
│   └── sockets.py
│   └── storage.py
├── tests
│   └── cli.py
├── .gitignore
├── Dockerfile
├── kv
├── main.py
├── README.md
├── requirements.txt
├── utils.py
├── test.py
├── tox.ini
```

- **main.py**

This contains main function which initialize the flask server. We add routing for class here.

- **utils.py**

This includes logger function which helps in logging in the application.

- **kv/resource.py**

This contains KeyValueStore class which have our get and put functions. This will handle the main functionality of server. It helps in retrieving value of key and setting values of key-value pairs.

- **kv/storage.py**

This file is being used to handle the storage feature of the application. It is being used for reading and writing data from file. We also create the file if it doesn't exist in this.

- **kv/sockets.py**

This contains sockets which are being used to broadcast events whenever there will be new updates in key value pair.

- **kv**

This is the client which can be used as a CLI. It supports three commands - get, put and watch. This uses requests module to call api's running on web server and also connects to socket of server.

- **requirements.txt**

This contains all required packages which can be installed using pip.
```
pip install -r requirements.txt
```

- **test.py**

This file contains basic tests which are configured according to this code base. It has tests which verifies the output from the server.

- **tests/cli.py**

This contains sample code of CLI. It is being used by the test.py file to execute testing.

---

## 🔨 CI/CD

This repo is configured with auto builds on every push to main branch. It occurs in three steps and every step is dependent on previous step. So if lint fails it won't build the image.

Steps:-

- **lint** - Lints the codebase using flake8
- **build** - Builds the dockerfile and pushes to registry with 2 tags - `latest` and `<commit-id>`.
- **test** - Some basic smoke tests are performed on the server.

---

## 🔧 Testing

There is linting and basic smoke testing setup in this codebase to prevent errors.

- **Linting**

Linting is enabled in CI - Github actions. It runs when a new PR is raised for `main` branch and also runs on new push on main branch.
Flake8 is being used to lint the codebase.

- **Smoke tests**

Some basic tests are configured which verifies if we are getting the expected output from the server.

`tox` - Tox helps in running tests, configuring the test tool of choice.
`pytest` - pytest is the tool being used to conduct testing.

`test.py` - This file contains basic test cases. It calls the `tests/cli.py` which contains code for CLI. It executes the cli commands and verifies the output. It throws error in case the output does not match the condition. More information on the testcasds are present in the docstrings of functions.