#!/bin/bash
set -e

# Create output directory
mkdir -p app/bin

# Compile the main.cpp file
g++ src/main.cpp -o app/bin/app
