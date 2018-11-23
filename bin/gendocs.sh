#!/usr/bin/env bash

BASE_DIR=$(dirname $0)/..

make -C $BASE_DIR/etc/sphinx clean html coverage

$BASE_DIR/bin/chkdocs.py
RET=$?
if [[ RET != 0 ]]
then
    echo "Documentation coverage is incomplete!"
    exit $RET
fi
