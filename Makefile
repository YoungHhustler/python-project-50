#Makefile

lint:
	poetry run flake8 gendiff

.PHONY: 