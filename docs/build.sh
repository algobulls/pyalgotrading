#!/bin/bash

# Load the virtualenv

# Generate fresh module index .rst files
rm -rf ./source/pyalgotrading.*rst
sphinx-apidoc -o ./source/ ../

# Build the html
source /home/algobulls/virtualenvs/pyalgotrading/bin/activate
make html

