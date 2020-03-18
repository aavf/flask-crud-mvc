Basic CRUD, verifies existing username, action messsages

## Virtual enviroment
### Install and activate
In a terminal, from project folder:

```
python2 -m virtualenv venv

source venv/bin/activate

pip install -r requirements.txt

# IN CASE OF MYSQL-PYTHON ERROR:
sudo env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install MySQL-python
```

## Run
```
$ export FLASK_CONFIG=development
$ export FLASK_APP=run.py
$ flask run
```

### test users
Username: admin

Password: admin


Username: user

Password: user