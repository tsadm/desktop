#!/usr/bin/env bash

set -e

if test $TRAVIS_OS_NAME == 'osx'; then
    brew update
    brew install python
    brew install python3
    pip3 install virtualenv
    make virtualenv
    exit 0
fi

if test $TRAVIS_OS_NAME == 'linux'; then
    pip install coverage
    pip install codecov
    python setup.py install
    exit 0
fi

exit 128
