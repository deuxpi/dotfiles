#!/bin/sh

set -e

PLATFORM=`uname`

if [[ "$PLATFORM" == 'Linux' ]]; then
  if [[ ! -x /usr/bin/rake ]]; then
    sudo apt-get install --no-install-recommends rake
  fi
fi

if [[ "$PLATFORM" == 'Darwin' ]]; then
  if [[ ! -x /usr/local/bin/brew ]]; then
    # Homebrew (https://brew.sh)
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  fi
fi

exec rake install
