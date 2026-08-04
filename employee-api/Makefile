up:
	docker compose up --build

down:
	docker compose down

restart:
	docker compose down
	docker compose up --build

logs:
	docker compose logs -f

ps:
	docker ps

build:
	docker compose build

health:
	curl http://localhost:5000/health

clean:
	docker compose down -v
