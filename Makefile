-include .env

create-network:
	docker network create $(NETWORK_NAME) || echo "Network already exists"

up:
	docker compose build && docker compose up -d && docker compose logs -f

logs:
	docker compose logs -f
