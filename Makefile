.PHONY: dev
dev:
	FLASK_APP=./app/app.py FLASK_ENV=development flask run

test:
	PYTHONPATH=. pytest -s

lint:
	pylint --load-plugins pylint_flask_sqlalchemy app

black:
	black --target-version=py39 .

db_prepare:
	FLASK_APP=./app/app.py flask db stamp head && flask db migrate

migrate_up:
	FLASK_APP=./app/app.py flask db upgrade

migrate_down:
	FLASK_APP=./app/app.py flask db downgrade

migrate:
	FLASK_APP=./app/app.py flask db migrate