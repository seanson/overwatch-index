WORKING_DIR := $(shell pwd)
WEBSITE_CNAME := overwatch.website

.DEFAULT_GOAL := docker-test

.PHONY: build push

generate:: ## Generates the static HTML
		@rm -fr dist && mkdir -p dist
		@poetry run python src/generate.py
		@cp -rv static dist/static

publish:: generate ## Publish content to the gh-pages branch
		@git fetch origin gh-pages:gh-pages -v
		@poetry run ghp-import -p dist -c ${WEBSITE_CNAME}

fetch:: ## Pulls down the newest set of content
		@poetry run python src/fetch.py

test:: ## Runs tests (TBD)
		@poetry run python -m pytest


# a help target including self-documenting targets (see the awk statement)
define HELP_TEXT
Usage: make [TARGET]... [MAKEVAR1=SOMETHING]...

Available targets:
endef
export HELP_TEXT
help: ## this help target
	@cat .banner
	@echo
	@echo "$$HELP_TEXT"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / \
		{printf "\033[36m%-30s\033[0m  %s\n", $$1, $$2}' $(MAKEFILE_LIST)
