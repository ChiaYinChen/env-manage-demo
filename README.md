# env-manage-demo

Managing environment variables using [dotenv](https://github.com/theskumar/python-dotenv) and [pydantic](https://github.com/samuelcolvin/pydantic).

## Environments

python 3.8.2
python-dotenv 0.19.0
pydantic 1.8.2

## Environment Variables

**.env**

```
MODE=PRODUCTION
```

**.test.env**

```
DB_HOST=127.0.0.1
DB_PORT=6666
DB_PASSWORD=testpass
DBCONN_STR=${DB_HOST}:${DB_PORT}
```

**.prod.env**

```
DB_HOST=localhost
DB_PORT=8888
DB_PASSWORD=prodpass
DBCONN_STR=${DB_HOST}:${DB_PORT}
BLAH_BLAH=Haha
```

## Run a demo

run:

```
$ python demo.py
```

result:

```
Before load_dotenv() None
{'API_BASE': 'https://testing.example.com/api',
 'DBCONN_STR': '127.0.0.1:6666',
 'DB_HOST': '127.0.0.1',
 'DB_NAME': 'testing',
 'DB_PASSWORD': 'testpass',
 'DB_PORT': 6666,
 'DEBUG': True}

After load_dotenv() PRODUCTION
{'API_BASE': 'https://example.com/api',
 'DBCONN_STR': 'localhost:8888',
 'DB_HOST': 'localhost',
 'DB_NAME': 'production',
 'DB_PASSWORD': 'prodpass',
 'DB_PORT': 8888,
 'DEBUG': False}
```
