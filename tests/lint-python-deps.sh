#!/bin/bash

# Basic Python Dependency Checking

# klude for OCP
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )
. ${DIR}/uid-kludge.sh

# Setup python virtual env
pip install -q -r requirements.txt
pip install -q -U pip

# pip freeze
echo -e "\nRUN: pip freeze\n"
pip freeze

# install dep tools
PIP_OTHER='johnnydep pipdeptree pip-check-reqs pur'
pip install -q ${PIP_OTHER}

# Run pip-check-reqs
echo -e "\nRUN: pip-missing-reqs\n"
pip-missing-reqs --ignore-file=tests/* .
echo -e "\nRUN: pip-extra-reqs\n"
pip-extra-reqs -r gunicorn --ignore-file=tests/* .

# Run pur
# echo -e "\nRUN: pur -r requirements.txt\n"
# pur -r requirements.txt --index-url $PIP_INDEX_URL --index-url $PIP_EXTRA_INDEX_URL 2>/dev/null
# pur doesn't work well offline in CI

echo -e "\nNOTE: you can try to use the following to update your requirements.txt"
echo -e "  pur -r requierments.txt"

# Run pip
echo -e "\nRUN: pip list --outdated\n"
pip list --outdated

# Run johnnydep
echo -e "\nRUN: johnnydep on requirements.txt\n"
for dep in $(egrep -v '#|^$' requirements.txt)
do
  echo -e "\nCHECK: dependencies for $dep\n"
  johnnydep $dep 2> /dev/null
done

# Run pipdeptree
echo -e "\nRUN: pipdeptree\n"
pipdeptree -e "$(echo $PIP_OTHER | tr ' ' ',')"
echo -e "\nRUN: pipdeptree --reverse\n"
pipdeptree -r -e "$(echo $PIP_OTHER | tr ' ' ',')"
