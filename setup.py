#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='certifier',
    version='0.2',
    url='https://github.com/mrsmn/certifier',
    download_url='https://github.com/mrsmn/certifier/archive/master.zip',
    author='Martin Simon',
    author_email='me@martinsimon.me',
    license='Apache v2.0 License',
    packages=['certifier'],
    description='Get all the information you need about your SSL certificates.',
    long_description=file('README.md','r').read(),
    keywords=[''],
)
