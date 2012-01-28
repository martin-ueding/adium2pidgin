#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

import optparse
import xml
import xml.dom.minidom

def parse(filename, read_format):
    if read_format == "adium":
        read_parser = parse_adium

    return read_parser(filename)

def parse_adium(filename):
    tree = xml.dom.minidom.parse(filename)
    
    chatobject = tree.childNodes[0]
    account = chatobject.getAttribute("account")
    service = chatobject.getAttribute("service")
    messages = chatobject.childNodes

    m_list = []

    for message in messages:
        if not message.nodeName == "message":
            continue

        alias = message.getAttribute("alias")
        sender = message.getAttribute("sender")
        time = message.getAttribute("time")

        child = message
        while child.nodeType != xml.dom.Node.TEXT_NODE:
            child = child.childNodes[0]

        text = child.nodeValue

        m = {"time": time, "alias": alias, "text": text, "sender": sender}
        m_list.append(m)

    c = {"messages": m_list, "account": account, "service": service}

    return c
