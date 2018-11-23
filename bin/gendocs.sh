#!/usr/bin/env bash

BASE_DIR=$(dirname $0)/..
make -C $BASE_DIR/etc/sphinx clean html coverage
./chk_docs.py

# TODO check return value

