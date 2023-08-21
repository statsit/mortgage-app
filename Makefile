.PHONY: all install_deps start_web docker_build

all: start_web  

install_deps:
	@echo "Installing dependencies..."
	poetry install

start_web:
	@echo "Starting web server..."
	poetry run uvicorn mortgage_app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000


docker_build:
	@echo "Building docker image..."
	docker-compose up -d --build