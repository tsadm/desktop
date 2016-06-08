PYTHON ?= python3

.PHONY: default
default: compile

.PHONY: clean
clean:
	@rm -rf .coverage htmlcov
	@$(PYTHON) setup.py clean -a 2>/dev/null
	@rm -rf dist tsdesktop.egg-info
	@find lib/ -type d -name __pycache__ | xargs rm -rfv

.PHONY: compile
compile:
	@$(PYTHON) -m compileall -x '*.egg-info' -x '.*_test\.py' lib/

.PHONY: build
build:
	@$(PYTHON) setup.py build

.PHONY: install
install: build
	@$(PYTHON) setup.py install

.PHONY: test
test:
	@make compile >/dev/null
	@$(PYTHON) test.py

.PHONY: test-v
test-v:
	@make compile >/dev/null
	@$(PYTHON) test.py -v

.PHONY: test-coverage
test-coverage:
	@make compile >/dev/null
	@$(PYTHON) -m coverage run --source='.' test.py
	@$(PYTHON) -m coverage report
	@$(PYTHON) -m coverage html

.PHONY: venv
venv:
	@$(PYTHON) -m virtualenv -p $(PYTHON) venv
	@venv/bin/python setup.py install
