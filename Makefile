.PHONY: run
run:
	poetry run python qsp/cli.py

.PHONY: isort
isort:
	poetry run isort .

.PHONY: linter
linter: isort
	poetry run black . 