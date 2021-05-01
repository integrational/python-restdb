#!/bin/sh

# ensure virtualenv is installed
python3 -m pip install --upgrade virtualenv

# create new virtual env in .venv in this project
virtualenv .venv

# could now run:
# .venv/bin/activate
# but prefer to run commands in .venv/bin/ explicitly
