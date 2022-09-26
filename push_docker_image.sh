#!/usr/bin/env bash
tag=$1
docker push -t docker.io/paritypr/do_nothing_app:"${tag}" 
