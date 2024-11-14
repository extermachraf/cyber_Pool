# Makefile
build:
	docker build -t victim .

run:
	docker run --rm --name victim -d victim

stop:
	docker stop victim

clean:
	docker rmi victim