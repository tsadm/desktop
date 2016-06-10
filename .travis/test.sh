#!/usr/bin/env bash

set -e

if test $TRAVIS_OS_NAME == 'osx'; then
    make test-all
    exit 0
fi

if test $TRAVIS_OS_NAME == 'linux'; then
    coverage run --source='.' test.py
    coverage report
    codecov
    exit 0
fi

exit 128
