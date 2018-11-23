#!/usr/bin/env bash

sphinx-apidoc -Me  -o source/apidoc ../src/typhon/
sphinx-build -b html -d build/doctrees   source build/html
