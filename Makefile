PREFIX ?= /usr/local

.PHONY: default
default: compile

.PHONY: clean
clean:
	@find . -type d -name __pycache__ | xargs rm -rfv
	@rm -vf lib/tsdesktop.zip

.PHONY: compile
compile:
	@python3 -m compileall -x '.*_test\.py' lib/


lib/tsdesktop.zip: compile
	@cd lib && zip -9r tsdesktop.zip \
		tsdesktop/*.py \
		tsdesktop/__pycache__ \
		-x '*_test.*.py[co]'

.PHONY: build
build: lib/tsdesktop.zip

.PHONY: install
install: build
	@mkdir -vp $(PREFIX)/bin
	@mkdir -vp $(PREFIX)/lib
	@install -v -m 755 bin/tsdesktop.py $(PREFIX)/bin/tsdesktop
	@install -v -m 644 lib/tsdesktop.zip $(PREFIX)/lib/tsdesktop.zip

.PHONY: test
test:
	@tests/run.bash
