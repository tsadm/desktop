#!/usr/bin/env bash

set -x

test -x $(which brew) || {
    echo "ERROR brew command line tools seems not to be installed!!"
    echo "ERROR check Homebrew web site for installing: http://brew.sh"
    exit 1
}

brew update

brew tap caskroom/cask
brew cask install virtualbox

for pkg in python python3 docker docker-machine; do
    brew install $pkg
done

docker-machine create --driver virtualbox default

exit 0
