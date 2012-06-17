#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

###############################################################################
#                                   License                                   #
###############################################################################
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.

"""
Tests the various modules.
"""

import unittest

import chatlogparser
import chatlogwriter

class ChatlogwriterTest(unittest.TestCase):
    def testJsonWriter(self):
        # TODO Implement test.
        assert True

    def testPidginWriter(self):
        # TODO Implement test.
        assert True

class ChatlogparserTest(unittest.TestCase):
    def testPidginParser(self):
        # TODO Implement test.
        assert True

    def testAdiumParser(self):
        # TODO Implement test.
        assert True

    def testJsonParser(self):
        # TODO Implement test.
        assert True

if __name__ == "__main__":
    unittest.main()
