#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

"""
Tests the various modules.
"""

import unittest

import chatlogparser
import chatlogwriter

class ChatlogwriterTest(unittest.TestCase):
    def testJsonWriter(self):
        assert True

    def testPidginWriter(self):
        assert True

class ChatlogparserTest(unittest.TestCase):
    def testPidginParser(self):
        assert True

    def testAdiumParser(self):
        assert True

    def testJsonParser(self):
        assert True

if __name__ == "__main__":
    unittest.main()
