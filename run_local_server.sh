#!/usr/bin/env bash
docker run --rm --name do_nothing_app -d -p 127.0.0.1:8000:8000 paritypr/do_nothing_app:0.0.1