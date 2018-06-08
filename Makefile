.PHONY: watch build

watch:
	watchman-make -p '*.py' 'Makefile' 'Dockerfile.web' '.dockerignore' -t build

build:
	docker rm -f web 2> /dev/null || true
	docker build -t web . -f Dockerfile.web
	# -i allows for docker attach to work with pdb
	docker run -i -d -p8080:8080 --name web web
