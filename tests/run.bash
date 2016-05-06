#!/usr/bin/env bash
SUITE=${1:-'tsdesktop'}
export PYTHONPATH=`dirname $0`/../lib
python3 -m unittest discover ${SUITE} -p '*_test.py'
