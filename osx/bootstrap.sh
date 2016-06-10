#!/usr/bin/env bash

set -e

brew update

brew tap caskroom/cask
brew cask install virtualbox

for pkg in python python3 docker docker-machine; do
    brew install $pkg
done

docker-machine create --driver virtualbox default

exit 0
