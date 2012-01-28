#!/usr/bin/python
# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

from xml.dom.minidom import parse
import xml
import optparse
import datetime
import dateutil.parser

import chat

def parse_adium(filename):
    tree = parse(filename)
    
    chatobject = tree.childNodes[0]
    account = chatobject.getAttribute("account")
    messages = chatobject.childNodes

    print account

    m_list = []

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

        m = chat.Message(time=time, alias=alias, text=text, sender=sender)
        m_list.append(m)

    c = chat.Chat(m_list)

    return c
