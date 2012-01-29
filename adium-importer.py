#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

import optparse
import json
import sys

import chatlogparser
import chatlogwriter

def main():
    options, args = _parse_args()

    filename = args[0]

    imported = parser.parse(filename, options.read_format)

    if options.outfile is not None:
        outfile = open(options.outfile, "w")
    else:
        outfile = sys.stdout

    writer.write(imported, outfile, options.write_format)

    if options.outfile is not None:
        outfile.close()

def _parse_args():
    """
    Parses the command line arguments.

    @return: Tuple with options and (positional) arguments.
    @rtype: tuple
    """
    parser = optparse.OptionParser(usage="", description="")
    parser.add_option("-o", dest="outfile", default=None, help="File to write to")
    parser.add_option("-w", dest="write_format", default="pidgin", help="Write format. [default: %default]")
    parser.add_option("-r", dest="read_format", default="adium", help="Read format. [default: %default]")

    return parser.parse_args()


if __name__ == "__main__":
    main()
