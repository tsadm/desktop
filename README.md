# tsdesktop [![Build Status](https://travis-ci.org/tsadm/desktop.svg?branch=master)](https://travis-ci.org/tsadm/desktop) [![codecov](https://codecov.io/gh/tsadm/desktop/branch/master/graph/badge.svg)](https://codecov.io/gh/tsadm/desktop)

tsadm desktop client - docker based environments for running web sites locally

## requirements

Python3 (>=3.4.4) or Python2 (>=2.7.10)
Docker (>=1.8.2)

Install dependencies: [GNU/Linux](docs/linux-deps.md) - [Mac OSX](docs/osx-deps.md)

## install using pip

> ~$ pip3 install https://github.com/tsadm/desktop/tarball/master

## run from source

> ~$ mkdir -vp src/tsadm && cd src/tsadm
>
> tsadm$ git clone https://github.com/tsadm/desktop.git

$HOME/src/tsadm/desktop/bin should be added to the PATH environment variable:

> ~$ echo 'export PATH=$HOME/src/tsadm/desktop/bin:$PATH' >>.bash_profile
>
> ~$ exec bash

## usage

> ~$ tsdesktop

Then access the web interface at `http://localhost:3680/`.

If you need to use a different port for the web interface, use `-p PORT`:

> ~$ tsdesktop -p 8080
