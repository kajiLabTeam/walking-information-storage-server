-include .env

up:
	docker compose build && docker compose up -d && docker compose logs -f

down:
	docker compose down --remove-orphans

destroy:
	docker compose down --rmi all --volumes

logs:
	docker compose logs -f

restart:
	rm -rf ./docker/postgres/data && docker compose down && docker compose build && docker compose up -d && docker compose logs -f


format:
	uv run ruff format && uv run ruff check --fix