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
Main script, interface to read and write various chatlog file formats.
"""

import optparse
import json
import sys

import chatlogparser
import chatlogwriter

__docformat__ = "restructuredtext en"

def main():
    options, args = _parse_args()

    filename = args[0]

    imported = chatlogparser.parse(filename, options.read_format)

    if options.outfile is not None:
        outfile = open(options.outfile, "w")
    else:
        outfile = sys.stdout

    chatlogwriter.write(imported, outfile, options.write_format)

    if options.outfile is not None:
        outfile.close()


def _parse_args():
    """
    Parses the command line arguments.

    :return: Tuple with options and (positional) arguments.
    :rtype: tuple
    """
    parser = optparse.OptionParser(usage="%prog [options] logfile", description="Parses chatlogs and writes them in other formats.")
    parser.add_option("-o", dest="outfile", default=None, help="File to write to")
    parser.add_option("-w", dest="write_format", default="pidgin", help="Write format. [default: %default]")
    parser.add_option("-r", dest="read_format", default="adium", help="Read format. [default: %default]")

    return parser.parse_args()


if __name__ == "__main__":
    main()
