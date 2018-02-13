#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import re
from setuptools import setup

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='itacate',
    version='1.0.0',
    url='https://github.com/categulario/itacate',
    license='BSD',
    author='Abraham Toriz Cruz',
    author_email='awonderfulcode@gmail.com',
    description='Configuration module from flask, for the rest of the world',
    long_description=readme,
    py_modules=['itacate'],
    platforms='any',
    install_requires=[],
    extras_require={
        'dev': [
            'pytest>=3',
            'tox',
        ],
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
