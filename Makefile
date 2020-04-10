# Author: Nick Russo
# Purpose: Provide simple "make" targets for developers
# See README for details about each target.

# Default goal runs the "test" target
.DEFAULT_GOAL := test

.PHONY: test
test: clean lint run

.PHONY: lint
lint:
	@echo "Starting  lint"
	find . -name "*.py" | xargs pylint
	find . -name "*.py" | xargs black -l 82 --check
	@echo "Completed lint"

.PHONY: run
run:
	@echo "Starting  run"
	python test.py
	@echo "Completed run"

.PHONY: clean
clean:
	@echo "Starting  clean"
	find . -name "*.pyc" | xargs -r rm
	@echo "Starting  clean"
