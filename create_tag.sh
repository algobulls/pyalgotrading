#!/usr/bin/env bash
set -e
VERSION="$(cat VERSION)"
git tag -a "$VERSION" -m "$VERSION"
