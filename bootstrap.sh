#!/bin/sh

set -e

PLATFORM=$(uname)

if [ "$PLATFORM" = 'Linux' ]; then
    if [ ! -x /usr/bin/rake ]; then
        sudo apt-get install --no-install-recommends rake
    fi
fi

exec rake install
