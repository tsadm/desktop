PYTHON ?= python3

.PHONY: default
default: compile

.PHONY: clean
clean:
	@rm -rf .coverage htmlcov
	@$(PYTHON) setup.py clean -a 2>/dev/null
	@rm -rf dist tsdesktop.egg-info
	@find lib/ -type d -name __pycache__ | xargs rm -rfv
	@find lib/ -type f -name '*.py[co]' | xargs rm -rfv

.PHONY: compile
compile:
	@#$(PYTHON) -m compileall -x '*.egg-info' -x '.*_test\.py' lib/
	@$(PYTHON) -m compileall lib/

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

.PHONY: test-py2
test-py2:
	@make test PYTHON=venv.py2/bin/python

.PHONY: test-py3
test-py3:
	@make test PYTHON=venv.py3/bin/python

.PHONY: test-all
test-all: test-py2 test-py3

.PHONY: test-coverage
test-coverage:
	@make compile >/dev/null
	@$(PYTHON) -m coverage run --source='.' test.py
	@$(PYTHON) -m coverage report
	@$(PYTHON) -m coverage html

.PHONY: virtualenv
virtualenv:
	@$(PYTHON) -m virtualenv -p python3 venv.py3
	@venv.py3/bin/python setup.py install
	@$(PYTHON) -m virtualenv -p python2 venv.py2
	@venv.py2/bin/python setup.py install

.PHONY: venv-travis
venv-travis:
	@$(PYTHON) -m virtualenv -p python3 venv.travis
	@venv.travis/bin/pip install coverage
	@venv.travis/bin/pip install codecov
