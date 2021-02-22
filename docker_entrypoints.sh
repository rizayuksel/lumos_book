echo "First Migrations"
python manage.py makemigrations

echo "First Migrate"
python manage.py migrate

echo "Run Project"
python manage.py runserver 0.0.0.0:8000

#bash -c "./docker_entrypoints.sh" ---> for docker-compose

python manage.py makemigrations book

python manage.py migrate

python manage.py makemigrations search

python manage.py migrate