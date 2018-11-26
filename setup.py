#!/usr/bin/env python3
# encoding: utf-8

from setuptools import setup
from codecs import open
from os import path

# get the long description from the README file
# here = path.abspath(path.dirname(__file__))
# with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
#     long_description = f.read()
with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='sysdfiles',
    version='0.1.0',
    license='MIT',
    description='systemd configuration file I/O',
    long_description=long_description,
    author='Shawn Baker',
    author_email='shawn@frozen.ca',
    url='https://github.com/ShawnBaker/sysdfiles',
    packages=['sysdfiles'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='systemd configuration files network_file',
    test_suite = 'nose.collector'
)
