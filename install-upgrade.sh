#!/bin/sh

bin=.venv/bin
pip=$bin/pip

# install generic Python tooling
$pip install --upgrade pycodestyle autopep8 pylint rope

# install packages specific to this project
$pip install --upgrade requests

# record all dependencies at their current version
$pip freeze > requirements.txt
