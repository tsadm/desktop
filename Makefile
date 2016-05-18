PYTHON ?= python3

.PHONY: default
default: compile

.PHONY: clean
clean:
	@rm -rf .coverage htmlcov
	@$(PYTHON) setup.py clean -a
	@rm -rf dist lib/tsdesktop.egg-info
	@find . -type d -name __pycache__ | xargs rm -rfv

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
