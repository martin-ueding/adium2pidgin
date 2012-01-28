#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

import optparse
import json

import parser

def main():
    options, args = _parse_args()

    filename = args[0]

    imported = parser.parse_adium(filename)

    print json.dumps(imported, sort_keys=True, indent=4)


def _parse_args():
    """
    Parses the command line arguments.

    @return: Tuple with options and (positional) arguments.
    @rtype: tuple
    """
    parser = optparse.OptionParser(usage="", description="")
    #parser.add_option("", dest="", type="", default=, help=)

    return parser.parse_args()


if __name__ == "__main__":
    main()
