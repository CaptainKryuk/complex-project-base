build: ;
	docker build -f docker/backend.dockerfile -t products-backend:latest .
	cd frontend && npm install

#build-frontend: ;
#	docker build -f docker/frontend.dockerfile -t products-frontend:latest .

up: ;
	docker-compose -f docker/docker-compose.yml -p products up -d --build
	docker exec -i -t -d pr-frontend sh -c "npm install && npm run dev"

down: ;
	docker-compose -f docker/docker-compose.yml -p products down -t 0

delete: ;
	docker-compose -f docker/docker-compose.yml -p products down -t 0 -v


# Proxy django manage.py commands

# https://stackoverflow.com/questions/2214575/passing-arguments-to-make-run
ifeq (dj, $(firstword $(MAKECMDGOALS)))
  RUN_ARGS := $(wordlist 2, $(words $(MAKECMDGOALS)), $(MAKECMDGOALS))
  $(eval $(RUN_ARGS):;@:)
endif

dj:
	docker exec -it pr-backend ./manage.py $(filter-out $@, $(MAKECMDGOALS))