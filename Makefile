# Variables
PYTHONPATH := $(shell pwd)

test:
	@pytest -svv --cov=src tests/ --cov-report xml

cov:
	coverage report -m

setup:
	@echo "---- Installing Python Dependencies ----"
	@pip install -r requirements.txt

run:
	@echo "---- Running Application ----"
	@PYTHONPATH="${PYTHONPATH}" python main.py

clean:
	@echo "---- Cleaning up .pyc files ----"
	@find . -name '*.pyc' -delete
	@echo "---- Cleaned ----"
