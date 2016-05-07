PREFIX ?= ${HOME}

.PHONY: default
default: compile

.PHONY: clean
clean:
	@find . -type d -name __pycache__ | xargs rm -rfv
	@rm -vf tsdesktop.bin lib/tsdesktop.zip
	@rm -rf .coverage htmlcov

.PHONY: compile
compile:
	@python3 -m compileall -x '.*_test\.py' lib/

lib/tsdesktop.zip: compile
	@cp -a lib/tsdesktop/buildinfo.py lib/tsdesktop/buildinfo.py.orig
	@echo "ID = '$(shell git log -n1 | head -n1 | cut -d ' ' -f 2)'" >lib/tsdesktop/buildinfo.py
	@echo "DATE = '$(shell date '+%Y-%m-%d')'" >>lib/tsdesktop/buildinfo.py
	@echo "FULLDATE = '$(shell date -R)'" >>lib/tsdesktop/buildinfo.py
	@echo "AUTHOR = '$(shell id -un)@$(shell hostname -s)'" >>lib/tsdesktop/buildinfo.py
	@cd lib && zip -q9r tsdesktop.zip __main__.py __pycache__/ \
		tsdesktop/*.py tsdesktop/__pycache__/ \
		-x '*_test.py' \
		-x '*_test.*.py[co]'
	@cat lib/tsdesktop/buildinfo.py.orig >lib/tsdesktop/buildinfo.py
	@rm -f lib/tsdesktop/buildinfo.py.orig

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
test:
	@make clean >/dev/null
	@make compile >/dev/null
	@python3 test.py

.PHONY: test-v
test-v:
	@make clean >/dev/null
	@make compile >/dev/null
	@python3 test.py -v

.PHONY: test-coverage
test-coverage:
	@make clean >/dev/null
	@make compile >/dev/null
	@python3 -m coverage run --source='.' test.py
	@python3 -m coverage report
	@python3 -m coverage html
