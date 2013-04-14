#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright © 2013 Martin Ueding <dev@martin-ueding.de>

from distutils.core import setup

__docformat__="restructuredtext en"

setup(
    author="Martin Ueding",
    author_email="dev@martin-ueding.de",
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Programming Language :: Python",

    ],
    #description="",
    download_url="http://martin-ueding.de/download/adium2pidgin/",
    license="GPLv2+",
    #long_description ="",
    name="adium2pidgin",
    py_modules=[
        'chatlogparser',
        'chatlogwriter',
        'tests',
    ],
    scripts=['adium2pidgin'],
    url="http://martin-ueding.de/projects/adium2pidgin/",
    version="1.0",
)
