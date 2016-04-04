#!/bin/bash

autoreconf --install
mkdir out
cd out
../configure --without-imagemagick --without-python --without-qt --with-jpeg 'CFLAGS=-O0 -g'
