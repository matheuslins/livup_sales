# Variables
PYTHONPATH := $(shell pwd)

test:
	@pytest -svv --cov=src tests/ --cov-report xml

cov:
	coverage report -m

setup:
	@echo "---- Installing Python Dependencies ----"
	@pip install -r requirements.txt --upgrade

setup_dev:
	@echo "---- Installing Dev Python Dependencies ----"
	@if [[ ! -e .env ]]; then \
		cp .env-example .env ; \
	fi
	@pip install -r requirements-dev.txt --upgrade

run:
	@echo "---- Running Application ----"
	@PYTHONPATH="${PYTHONPATH}" python main.py

clean:
	@echo "---- Cleaning up .pyc files ----"
	@find . -name '*.pyc' -delete
	@echo "---- Cleaned ----"
