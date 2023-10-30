#!/bin/sh

## Usage:
##   . ./export-env.sh;

export $(grep -v "^#" .env | xargs -d "\n")