#!/bin/bash

# Exit if any command fails
set -e

echo "Running C++ linter (cppcheck)..."

# Run cppcheck on the src/ and include/ folders
cppcheck --enable=all --inconclusive --std=c++11 --quiet src include

echo "Linting complete! ✅"
