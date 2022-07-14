#!/bin/bash

# Basic Python Linting

# klude for OCP
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )
. ${DIR}/uid-kludge.sh

# Setup python virtual env
pip install -q -r requirements.txt
pip install -q pylint mypy

# Run pylint with minimum score
echo -e "\nRUN: pylint\n"
find * -type f -name "*.py" | xargs pylint --fail-under=4 || echo -e "\nFAILED: but ignoring\n"

# Run mypy
echo -e "\nRUN: mypy\n"
find * -type f -name "*.py" | xargs mypy --ignore-missing-imports --strict || echo -e "\nFAILED: but ignoring\n"
