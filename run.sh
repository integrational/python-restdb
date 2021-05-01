#!/bin/sh

bin=.venv/bin

$bin/pycodestyle --ignore=E241,E501 *.py
$bin/pylint --score=n --disable=C,W0104 *.py
$bin/python main.py $*
