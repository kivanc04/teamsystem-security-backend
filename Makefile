.PHONY: test run docker-up docker-down logs

test:
	python -m pytest -q

run:
	uvicorn app.main:app --reload --port 8001

docker-up:
	docker compose up --build -d

docker-down:
	docker compose down --remove-orphans

logs:
	docker compose logs -f api
