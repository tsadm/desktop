.PHONY: default
default:

.PHONY: pull-deps
pull-deps:
	docker pull debian

.PHONY: build
build:
	docker build -t tsadm/desktop base
	docker build -t tsadm/desktop:mysqld mysqld
	docker build -t tsadm/desktop:httpd httpd
