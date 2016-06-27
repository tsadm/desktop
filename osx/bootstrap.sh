#!/usr/bin/env bash

set -x

test -x $(which brew) || {
    echo "ERROR brew command line tools seems not to be installed!!"
    echo "ERROR check Homebrew web site for installing: http://brew.sh"
    exit 1
}

brew update

brew install python
brew install python3

if test $1 != '--testing'; then
    brew tap caskroom/cask
    brew cask install virtualbox

    brew install docker
    brew install docker-machine

    docker-machine create --driver virtualbox default
fi

exit 0
