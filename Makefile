##	help:	This.
.PHONY: help
.DEFAULT: help
help: Makefile
#	Find all double comments and treat them as docstrings
	@echo "make <command>"
	@sed -n 's/^##//p' $<
#	TODO: The following commands
#	@echo "make lint"
#	@echo "		TBD run static code analysers"
	@echo "make test"
	@echo "		TBD run tests"
#	@echo "make docs"
#	@echo "		TBD build docs"
# serve docs (hot-reload); coverage?

## 	watch:	Hot-reload web-app server.
.PHONY: watch
watch:
#	Build files in case they changed while we were not watching
	$(MAKE) build
	watchman-make -p '*.py' 'Makefile' 'Dockerfile.web' '.dockerignore' -t build

##	build:	Build & run (in the background) the web-app server.
.PHONY: build
build:
#	Kill the currently running container before re-building because
#	docker does not detect that it has changed
	docker rm -f web 2> /dev/null || true
	docker build -t web . -f Dockerfile.web
#	-i allows for docker attach to work with pdb
#   -t gives coloured output
	docker run -it -d -p8080:8080 --name web web


.PHONY: test
test:
#	unit-tests
	pipenv run pytest web/*
#	integration tests
	docker build -t integration_tests . -f integration_tests.Dockerfile
	docker run -it --rm --network container:web integration_tests
