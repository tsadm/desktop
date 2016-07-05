# tsdesktop [![Build Status](https://travis-ci.org/tsadm/desktop.svg?branch=master)](https://travis-ci.org/tsadm/desktop) [![codecov](https://codecov.io/gh/tsadm/desktop/branch/master/graph/badge.svg)](https://codecov.io/gh/tsadm/desktop)

tsadm desktop client - docker based environments for running web sites locally

## Requirements

Python3 (>=3.4.4) or Python2 (>=2.7.10)
Docker (>=1.8.2)

Install dependencies: [GNU/Linux](docs/linux-deps.md) - [Mac OSX](docs/osx-deps.md)

## Install using pip

    pip3 install https://github.com/tsadm/desktop/tarball/master

## Run from source

    mkdir -vp src/tsadm && cd src/tsadm
    tsadm$ git clone https://github.com/tsadm/desktop.git

$HOME/src/tsadm/desktop/bin should be added to the PATH environment variable:

    echo 'export PATH=$HOME/src/tsadm/desktop/bin:$PATH' >>.bash_profile
    exec bash

## Usage

### Web interface

    tsdesktop

Then access the web interface at `http://localhost:3680/`.

If you need to use a different port for the web interface, use `-p PORT`:

    tsdesktop -p 8080

### Command line

Run `tsdesktop --help` for the full list of options.

#### Service container

    # start
    tsdesktop -S mysqld

    # stop
    tsdesktop -K mysqld

#### Site container

    # start
    tsdesktop -S httpd -s sitename

    # stop
    tsdesktop -K httpd -s sitename

#### Database tools

    # sql command line client
    tsdesktop -J dbname

    # import .sql and compressed .sql.gz files
    tsdesktop -J dbname <file.sql
    gunzip -c file.sql.gz | tsdesktop -J dbname
