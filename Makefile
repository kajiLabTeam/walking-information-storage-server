-include .env

up:
	docker compose build && docker compose up -d

db:
	docker exec -it $(POSTGRES_CONTAINER_HOST) psql -U $(POSTGRES_USER) -d $(POSTGRES_DB)

logs:
	docker compose logs -f