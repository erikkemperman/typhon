#!/usr/bin/env bash

THIS_DIR=$(dirname $0)
BASE_DIR=$THIS_DIR/..

make -C $BASE_DIR/etc/sphinx all
DOC_MAKE_RET=$?
if [[ $DOC_MAKE_RET != 0 ]]
then
    echo "Documentation build failed!"
    exit $DOC_MAKE_RET
fi


$THIS_DIR/chkdocs.py
DOC_COVERAGE_RET=$?
if [[ $DOC_COVERAGE_RET != 0 ]]
then
    echo "Documentation coverage is incomplete!"
    exit $DOC_COVERAGE_RET
fi
