#!/usr/bin/env bash

tag=$1

if (( $# != 1 )) ; then
  echo "You forgot the 'tag' argument"
  exit 1
fi

docker run --rm --name do_nothing_app -d -p 127.0.0.1:8000:8000 paritypr/do_nothing_app:"${tag}"