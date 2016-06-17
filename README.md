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

## site integration

tsdesktop uses as the *sitename* the name of the current directory, and your site's document root should be under a directory called *docroot*. For this example, the sitename would be `my-php-site` and the site should be installed under `$HOME/src/my-php-site/docroot` directory.

If the php site is a drupal site, it can be integrated with tsadm as explained in tsadm's help pages. (including /home/tsadm/drupal.settings.php).

Any plain HTML or php site should be able to run under the httpd container. If it requires a mysql database, it should be configured to connect to `tsdesktop-mysqld` server, as `sitename` user (ie: `my-php-site`) to `sitenamedb` database (ie: `my-php-sitedb`), with an empty password (ie: `""`).

Just a few basic php modules are installed in httpd container, mainly trying to keep its size at minimum, but more can be added as needed.
