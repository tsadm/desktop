PREFIX ?= ${HOME}

.PHONY: default
default: compile

.PHONY: clean
clean:
	@find . -type d -name __pycache__ | xargs rm -rfv
	@rm -vf tsdesktop.bin lib/tsdesktop.zip

.PHONY: compile
compile:
	@python3 -OO -m compileall -x '.*_test\.py' lib/

lib/tsdesktop.zip: compile
	@cd lib && zip -q9r tsdesktop.zip __main__.py __pycache__/ \
		tsdesktop/*.py tsdesktop/__pycache__/ \
		-x '*_test.py' \
		-x '*_test.*.py[co]'

tsdesktop.bin: lib/tsdesktop.zip
	@python3 -m zipapp -o tsdesktop.bin -p '/usr/bin/env python3' \
		lib/tsdesktop.zip

.PHONY: build
build: tsdesktop.bin

.PHONY: install
install: build
	@mkdir -vp $(PREFIX)/bin
	@install -v -m 755 tsdesktop.bin $(PREFIX)/bin/tsdesktop

.PHONY: test
test: compile
	@PYTHONPATH=${PWD}/lib python3 -m unittest \
		discover tsdesktop -p '*_test.py'
