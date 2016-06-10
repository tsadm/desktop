PYCMD ?= python3
TEST_ARGS ?=

.PHONY: default
default: compile

.PHONY: clean
clean:
	@rm -rf .coverage htmlcov
	@$(PYCMD) setup.py clean -a 2>/dev/null
	@rm -rf build dist tsdesktop.egg-info
	@find lib/ -type d -name __pycache__ | xargs rm -rfv
	@find lib/ -type f -name '*.py[co]' | xargs rm -rfv

.PHONY: compile
compile:
	@#$(PYCMD) -m compileall -x '*.egg-info' -x '.*_test\.py' lib/
	@$(PYCMD) -m compileall lib/

.PHONY: build
build:
	@$(PYCMD) setup.py build

.PHONY: install
install: build
	@$(PYCMD) setup.py install

.PHONY: test
test:
	@make compile >/dev/null
	@$(PYCMD) test.py $(TEST_ARGS)

.PHONY: test-py2
test-py2:
	@make -s test PYCMD=venv.py2/bin/python

.PHONY: test-py3
test-py3:
	@make -s test PYCMD=venv.py3/bin/python

.PHONY: test-all
test-all: test-py2 test-py3

.PHONY: test-coverage
test-coverage:
	@make compile >/dev/null
	@$(PYCMD) -m coverage run --source='lib/tsdesktop' test.py
	@$(PYCMD) -m coverage report
	@$(PYCMD) -m coverage html

.PHONY: virtualenv
virtualenv:
	@$(PYCMD) -m virtualenv -p python3 venv.py3
	@venv.py3/bin/python setup.py install
	@venv.py3/bin/pip install coverage
	@$(PYCMD) -m virtualenv -p python2 venv.py2
	@venv.py2/bin/python setup.py install
	@venv.py2/bin/pip install coverage
