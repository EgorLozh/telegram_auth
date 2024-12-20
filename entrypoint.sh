poetry run python telegram_auth/manage.py makemigrations
poetry run python telegram_auth/manage.py migrate
poetry run python telegram_auth/manage.py runserver 0.0.0.0:${API_PORT}