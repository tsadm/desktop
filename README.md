# tsdesktop [![Build Status](https://travis-ci.org/tsadm/desktop.svg?branch=master)](https://travis-ci.org/tsadm/desktop) [![codecov](https://codecov.io/gh/tsadm/desktop/branch/master/graph/badge.svg)](https://codecov.io/gh/tsadm/desktop)

tsadm desktop client - docker based environments for running web sites locally

## requirements

Python3 (>=3.4.4) and Docker are required dependencies for tsdesktop to work.

Python2 is not supported.

### install python

For Mac OSX you can download the latest Python3 realease from the official site: [Mac OSX](https://www.python.org/downloads/mac-osx/)

Most of GNU/Linux distributions already provide an installation of python3 or you can install it via the package manager, for Debian like systems:

> ~$ sudo apt-get install python3 python3-pip

### install docker

tsdesktop runs httpd, mysqld and other services using docker containers, so you need a working installation of docker before to start using this tool.

Official docs: [GNU/Linux](https://docs.docker.com/linux/step_one/) - [Mac OSX](https://docs.docker.com/mac/step_one/)

On Debian or Ubuntu systems, you can `sudo apt-get install docker.io`.

Under OSX systems you have to run tsdesktop from a *Docker Quickstart Terminal*.

## install using pip

> ~$ pip3 install https://github.com/tsadm/desktop/tarball/master

Under OSX you could need to do the following, in case Python bin dir is not already in PATH environment variable (check whith `echo $PATH`):

> ~$ echo 'export PATH=/Library/Frameworks/Python.framework/Versions/3.5/bin:$PATH' >>.bash_profile
>
> ~$ exec bash

## run from source

> ~$ mkdir -vp src/tsadm && cd src/tsadm
>
> tsadm$ git clone https://github.com/tsadm/desktop.git

$HOME/src/tsadm/desktop/bin should be added to the PATH environment variable:

> ~$ echo 'export PATH=$HOME/src/tsadm/desktop/bin:$PATH' >>.bash_profile
>
> ~$ exec bash

## pull docker images

> ~$ docker pull tsadm/desktop:httpd
>
> ~$ docker pull tsadm/desktop:mysqld

[docker.io images repository](https://hub.docker.com/r/tsadm/desktop/)

## usage

> ~$ cd src/my-php-site
>
> my-php-site$ tsdesktop -w
>
> \# do some work on site's code and test it at http://localhost:33380/
>
> \# type ^C (ctrl+c) to stop the httpd container and stop mysqld container then
>
> my-php-site$ tsdesktop -K mysqld

## site integration

tsdesktop uses as the *sitename* the name of the current directory, and your site's document root should be under a directory called *docroot*. For this example, the sitename would be `my-php-site` and the site should be installed under `$HOME/src/my-php-site/docroot` directory.

If the php site is a drupal site, it can be integrated with tsadm as explained in tsadm's help pages. (including /home/tsadm/drupal.settings.php).

Any plain HTML or php site should be able to run under the httpd container. If it requires a mysql database, it should be configured to connect to `tsdesktop-mysqld` server, as `sitename` user (ie: `my-php-site`) to `sitenamedb` database (ie: `my-php-sitedb`), with an empty password (ie: `""`).

Just a few basic php modules are installed in httpd container, mainly trying to keep its size at minimum, but more can be added as needed.

### import sql file to site's database

> my-php-site$ tsdesktop --sql-import dbdump.sql

The command above will import the .sql file to the site's database using the mysqld service container.

Databases are saved locally in your machine (not inside the container) under `~/.cache/tsdesktop` directory.
