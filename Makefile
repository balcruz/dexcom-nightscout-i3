.PHONY: install test run clean

install:
	@pip install -r requirements.txt
	@pip install -e .

test:
	@python -m unittest discover -s tests

run:
	@python -m src.nightscout.main

clean:
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -exec rm -f {} +
	@rm -rf .env
	@rm -rf venv

help:
	@echo "Available targets:"
	@echo "  install   Install dependencies and package"
	@echo "  test      Run tests"
	@echo "  run       Run the main script"
	@echo "  clean     Remove compiled Python files and virtual environment"
	@echo "  help      Show this help message"
