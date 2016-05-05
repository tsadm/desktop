.PHONY: default
default:

.PHONY: pull-deps
pull-deps:
	docker pull debian:stable

.PHONY: build
build:
	docker build -t tsdesktop/base base
	docker build -t tsdesktop/mysqld mysqld
	docker build -t tsdesktop/httpd httpd
