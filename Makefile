-include .env

up:
	docker compose build && docker compose up -d && docker compose logs -f

logs:
	docker compose logs -f
