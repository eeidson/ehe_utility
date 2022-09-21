#!/usr/bin/env python3
"""
############################################################################
Program:
    setup

Author:
    Hunter Eidson / eeidson@kennesaw.edu

Usage:
    setup.py <arg1> <arg2> ... <argN>

Version:
    0.1

Description:


TODO Notes:
    * Add internal tags for export control and other things as needed
############################################################################
@(#)setup.py     0.1 (Kennesaw State University) eeidson    15-Sep-2022
############################################################################
"""
from setuptools import setup


setup(
    name="ehe_utility",
    version="0.6.0",
    description="A generic utility module I use a lot",
    url="",
    author="Hunter Eidson",
    author_email="eeidson@gmail.com",
    license="GPL",
    packages=["ehe_utility"],
    install_requires=["humanize"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
)
