PREFIX ?= /usr/local

.PHONY: default
default: compile

.PHONY: clean
clean:
	@find . -type d -name __pycache__ | xargs rm -rfv
	@rm -vf tsdesktop.bin

.PHONY: compile
compile:
	@python3 -m compileall lib/

tsdesktop.bin: compile
	python3 -m zipapp lib -o tsdesktop.bin -p '/usr/bin/env python3' -m 'tsdesktop.cmd:main'

.PHONY: install
install: tsdesktop.bin
	@mkdir -vp $(PREFIX)/bin
	@install -v -m 755 tsdesktop.bin $(PREFIX)/bin/tsdesktop
