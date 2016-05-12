# tsdesktop [![Build Status](https://travis-ci.org/tsadm/desktop.svg?branch=master)](https://travis-ci.org/tsadm/desktop) [![codecov](https://codecov.io/gh/tsadm/desktop/branch/master/graph/badge.svg)](https://codecov.io/gh/tsadm/desktop)

tsadm desktop client - docker based environments for running web sites locally

## install

> ~$ mkdir -vp src/tsadm && cd src/tsadm
>
> tsadm$ git clone https://github.com/tsadm/desktop.git
>
> tsadm$ cd desktop
>
> desktop$ make install PREFIX=/usr/local

Try using sudo if you get write errors under /usr/local:

> desktop$ sudo make install PREFIX=/usr/local

Or install under your $HOME directory (the default PREFIX):

> desktop$ sudo make install

Either /usr/local/bin or $HOME/bin should be in your PATH environment variable. In order for the commands documented below to work.

## install docker

tsdesktop runs httpd, mysqld and other services using docker containers, so you need a working installation of docker before to start using this tool.

Official docs: [GNU/Linux](https://docs.docker.com/linux/step_one/) - [Mac OSX](https://docs.docker.com/mac/step_one/)

On Debian or Ubuntu systems, you can `apt-get install docker.io`.

Under OSX systems you have to run tsdesktop from a *Docker Quickstart Terminal*.

### pull tsdesktop docker images

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
