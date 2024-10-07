SHELL := /bin/bash
.PHONY: setup test

setup:
	rm -rf env
	python3 -m venv env
	/bin/bash -c "source ./env/bin/activate && pip install -r requirements.txt"

test:
	/bin/bash -c "source ./env/bin/activate && pytest"
