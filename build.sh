#!/usr/bin/env bash
tag=$1
docker build -t paritypr/do_nothing_app:"${tag}" .
