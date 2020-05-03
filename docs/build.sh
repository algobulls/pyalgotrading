#!/bin/bash

# Load the virtualenv
source /home/algobulls/virtualenvs/pyalgotrading/bin/activate

# Generate fresh module index .rst files
rm -rf ./source/pyalgotrading.*rst
sphinx-apidoc -o ./source/ ../pyalgotrading

# Build the html
make html

