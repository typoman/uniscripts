#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name="uniscripts",
    version="0.0.1",
    description="A python module for finding a script of a unicode character.",
    author="Bahman Eslami",
    author_email="contact@bahman.design",
    url="http://bahman.design",
    license="MIT",
    platforms=["Any"],
    package_dir={'': 'Lib'},
    packages=find_packages('Lib'),
)
