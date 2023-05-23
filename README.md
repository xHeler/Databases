# Databases
```sh
docker exec -it 791c9ecd4d52 ./cockroach sql --insecure
CREATE DATABASE mydatabase;
```

# Migration and init
```sh
export FLASK_APP=api.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```