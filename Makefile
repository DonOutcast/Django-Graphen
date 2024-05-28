.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: run
run: ## Run the FastAPI server
	@docker-compose --profile all up -d

.PHONY: stop
stop: ## Stop all containers
	@docker-compose --profile all down

.PHONY: version
version: ## Show the version of Docker Compose
	@docker-compose --version

.PHONY: run_db
run_db: ## Run just database
	@docker-compose --profile db up
