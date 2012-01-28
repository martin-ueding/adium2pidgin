#!/usr/bin/python
# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

from xml.dom.minidom import parse
import xml
import optparse
import datetime
import dateutil.parser

class Parser(object):
    """
    Parses a chatlog.
    """
    def parse(filename):
        """
        @rtype: Chat
        """
        pass


class AdiumParser(Parser):
    def parse(filename):
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
