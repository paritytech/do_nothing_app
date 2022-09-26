#!/usr/bin/env bash
tag=$1

if (( $# != 1 )) ; then
  echo "You forgot the 'tag' argument"
  exit 1
fi

docker push docker.io/paritypr/do_nothing_app:"${tag}" 
