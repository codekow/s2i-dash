#!/bin/bash

# Basic Python Security Scan

# klude for OCP
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )
. ${DIR}/uid-kludge.sh

# Setup python virtual env
pip install -q -r requirements.txt
pip install -q safety safety-db bandit

# Run Safety Report
echo -e "\nRUN: safety check -r requirements.txt\n"
safety check -r requirements.txt \
  --db $(pip show safety_db | grep Location | cut -d' ' -f2)/safety_db \
  --full-report

# Run Bandit Report-Only
echo -e "\nRUN: bandit\n"
bandit -r ./ || echo -e "\nFAILED: but ignoring\n"
