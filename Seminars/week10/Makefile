DOCKER-COMPOSE = docker compose
PYTHON = python -B

api:
	$(PYTHON) -m cli --start-api

docker:
	$(DOCKER-COMPOSE) down --remove-orphans
	$(DOCKER-COMPOSE) up --build

migrations-make:
	$(PYTHON) -m alembic revision --autogenerate --message "..."

migrations-up:
	$(PYTHON) -m alembic upgrade head
