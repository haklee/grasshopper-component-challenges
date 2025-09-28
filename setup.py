#!/usr/bin/env python
"""
Setup script for grasshopper-component-challenges package.
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_readme():
    try:
        with open("README.md", "r", encoding="utf-8") as fh:
            return fh.read()
    except TypeError:
        # Python 2 doesn't support encoding parameter
        with open("README.md", "r") as fh:
            return fh.read().decode('utf-8')

# Read version from version file
def read_version():
    version_file = os.path.join(os.path.dirname(__file__), "grasshopper_challenges", "__version__.py")
    if os.path.exists(version_file):
        try:
            with open(version_file, "r", encoding="utf-8") as f:
                return f.read().strip().split('"')[1]
        except TypeError:
            # Python 2 doesn't support encoding parameter
            with open(version_file, "r") as f:
                return f.read().decode('utf-8').strip().split('"')[1]
    return "0.1.0"

setup(
    name="grasshopper-component-challenges",
    version="0.1.0",
    author="Grasshopper Component Challenges Team",
    author_email="",
    description="A collection of coding challenges for Grasshopper components",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/grasshopper-component-challenges",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=2.7",
    install_requires=[
        # Add any dependencies here if needed
    ],
    include_package_data=True,
    package_data={
        "grasshopper_challenges": [
            "testcases/**/*",
            "judges/**/*",
        ],
    },
)
