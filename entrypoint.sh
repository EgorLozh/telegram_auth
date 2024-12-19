poetry run python telegram_auth/manage.py makemigrations
poetry run python telegram_auth/manage.py migrate
python manage.py createsuperuser --username=${ADMIN_NAME} --password=${ADMIN_PASSWORD}
poetry run python telegram_auth/manage.py runserver 0.0.0.0:${API_PORT}