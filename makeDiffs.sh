#!/usr/bin/env bash

# first make the following files the way you want them to be, commit then to git
# then call just the swagger-codegen line from generate.sh
# then call this script to generate the patches

git diff -R setup.py > patches/setup.patch
git diff -R README.md > patches/README.patch
git diff -R .travis.yml > patches/travis.patch
