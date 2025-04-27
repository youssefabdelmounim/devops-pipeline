#!/usr/bin/env python3

import os
import subprocess

def generate_coverage():
    print("Generating test coverage report...")

    # Make sure build directory exists
    if not os.path.exists('build'):
        os.makedirs('build')

    # Compile with coverage flags
    subprocess.run(['g++', '-fprofile-arcs', '-ftest-coverage', '-std=c++11',
                    '-Iinclude', 'tests/test_main.cpp', '-o', 'build/test_main'], check=True)

    # Run the test
    subprocess.run(['./build/test_main'], check=True)

    # Generate coverage report
    subprocess.run(['gcovr', '-r', '.', '--html', '--html-details', '-o', 'build/coverage.html'], check=True)

    print("Coverage report generated at build/coverage.html ✅")

if __name__ == "__main__":
    generate_coverage()
