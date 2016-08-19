#!/bin/bash

autoreconf --install
mkdir out
cd out
../configure --without-python --without-qt --with-jpeg 'CFLAGS=-O0 -g'
