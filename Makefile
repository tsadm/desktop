.PHONY: default
default: build

.PHONY: clean
clean:
	@find . -type d -name __pycache__ | xargs rm -rfv
	@rm -vf tsdesktop.bin

.PHONY: compile
compile:
	@python3 -m compileall lib/

.PHONY: build
build: compile
	@python3 -m zipapp lib/tsdesktop -o tsdesktop.bin -p '/usr/bin/env python3'
