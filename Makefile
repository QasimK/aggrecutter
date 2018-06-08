.PHONY: watch build

watch:
	watchman-make -p '*.py' 'Makefile' -t build

build:
	docker stop -t1 web 2> /dev/null || true
	docker build -t web . -f Dockerfile.web
	docker run -d -p8080:8080 --rm --name web web
