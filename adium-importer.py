#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

from xml.dom.minidom import parse
import xml
import optparse
import datetime
import dateutil.parser

def main():
    options, args = _parse_args()

    filename = args[0]

    tree = parse(filename)
    
    chatobject = tree.childNodes[0]
    account = chatobject.getAttribute("account")
    messages = chatobject.childNodes

    print account

    for message in messages:
        if not message.nodeName == "message":
            continue


        alias = message.getAttribute("alias")
        sender = message.getAttribute("sender")
        time = dateutil.parser.parse(message.getAttribute("time"))

        child = message
        while child.nodeType != xml.dom.Node.TEXT_NODE:
            child = child.childNodes[0]

        text = child.nodeValue

        print time, alias.rjust(20), ":", text



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
