.PHONY: install run test clean lint docker-build docker-run docker-dev docker-clean docker-logs docker-shell

# Local development commands
install:
	pip3 install -r requirements.txt

run:
	python3 app/api.py

run-prod:
	gunicorn --bind 0.0.0.0:5000 --chdir app api:app

lint:
	pip3 install flake8
	flake8 app/

test:
	pip3 install pytest
	pytest

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete

# Docker commands
docker-build:
	docker compose build

docker-build-prod:
	docker compose build api

docker-build-dev:
	docker compose build api-dev

docker-run:
	docker compose up api

docker-dev:
	docker compose up api-dev

docker-stop:
	docker compose down

docker-clean:
	docker compose down -v --rmi all
	docker system prune -f

docker-logs:
	docker compose logs -f

# Docker shell access
docker-shell-prod:
	docker compose exec api /bin/bash

docker-shell-dev:
	docker compose exec api-dev /bin/bash

# Docker tests
docker-test:
	docker compose run --rm api-dev pytest

# Docker linting
docker-lint:
	docker compose run --rm api-dev flake8 app/ 