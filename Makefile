DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
APP_COMPOSE_FILE = docker-compose/django_app.yaml
STORAGE_COMPOSE_FILE = docker-compose/storage.yaml
TG_BOT_COMPOSE_FILE = docker-compose/telegram_bot.yaml
BROKER_COMPOSE_FILE = docker-compose/broker.yaml
MANAGE_PY = python manage.py
APP_CONTAINER = django-app
ENV_FILE = .env

ARGS ?=


.PHONY: app
app:
	$(DC) --env-file $(ENV_FILE) -f $(APP_COMPOSE_FILE) up --build -d


.PHONY: app-down
app-down:
	$(DC) -f $(APP_COMPOSE_FILE) down


.PHONY: storage
storage:
	$(DC) --env-file $(ENV_FILE) -f $(STORAGE_COMPOSE_FILE) up --build -d


.PHONY: storage-down
storage-down:
	$(DC) -f $(STORAGE_COMPOSE_FILE) down


.PHONY: tg_bot
tg_bot:
	$(DC) -f $(TG_BOT_COMPOSE_FILE) up --build -d


.PHONY: tg_bot-down
tg_bot-down:
	$(DC) -f $(TG_BOT_COMPOSE_FILE) down


.PHONY: migrations
migrations:
	$(EXEC) $(APP_CONTAINER) poetry run $(MANAGE_PY) makemigrations


.PHONY: migrate
migrate:
	$(EXEC) $(APP_CONTAINER) poetry run $(MANAGE_PY) migrate


.PHONY: broker
broker:
	$(DC) --env-file $(ENV_FILE) -f $(BROKER_COMPOSE_FILE) up --build -d


.PHONY: broker-down
broker-down:
	$(DC) -f $(BROKER_COMPOSE_FILE) down

.PHONY: all
all:
	$(DC) --env-file $(ENV_FILE) -f $(APP_COMPOSE_FILE) -f $(STORAGE_COMPOSE_FILE) -f $(TG_BOT_COMPOSE_FILE) -f $(BROKER_COMPOSE_FILE) up --build -d


.PHONY: down
down: 
	$(DC) --env-file $(ENV_FILE) -f $(APP_COMPOSE_FILE) -f $(STORAGE_COMPOSE_FILE) -f $(TG_BOT_COMPOSE_FILE) -f $(BROKER_COMPOSE_FILE) down

.PHONY: restart
restart: down all



