#!/usr/bin/env bash
set -e
if ! pip freeze | grep -q twine; then
	echo "twine is not installed - please run 'pip install twine' to install"
	exit 1
fi
rm -rf dist
python setup.py bdist_wheel
twine upload --skip-existing dist/*
