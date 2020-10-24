# -*- coding: utf-8 -*-
"""
"""
from setuptools import setup, find_packages, Extension


setup(
    name='codesign-test',
    version='0.1.0',
    packages=find_packages(),
    ext_modules=[
        Extension(
            # the qualified name of the extension module to build
            'fib',
            # the files to compile into our module relative to ``setup.py``
            ['fib.c'],
        ),
    ],
)
