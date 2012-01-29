#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

import optparse
import re
import xml
import xml.dom.minidom

def parse(filename, read_format):
    """
    Parses a chatlog into a chat dict.

    @param filename: File to read.
    @type filename: str
    @param read_format: Format of the chatlog.
    @type read_format: str
    @rtype: dict
    """
    if read_format == "adium":
        read_parser = parse_adium
    elif read_format == "pidgin":
        read_parser = parse_pidgin

    return read_parser(filename)

def parse_adium(filename):
    """
    Parses an Adium chatlog.

    @param filename: File to read.
    @type filename: str
    @rtype: dict
    """
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

def parse_pidgin(filename):
    """
    Parses an Pidgin chatlog.

    @param filename: File to read.
    @type filename: str
    @rtype: dict
    """
    with open(filename) as f:
        filetext = f.read()
    
    #bla = re.compile(r'.*(\d+) at .* on (\d+).*')
    #m = bla.match("asd 123 at blabl asdj blo on 456 (bla) asd")
    m = re.match(r'.*<title>Conversation with (\d+) at .* on (\d+) \((\w+)\)</title>.*',filetext)
    if m is not None:
        print m.groups()
        print "found one"
    else:
        print "there is none"
    
    account = m.groups(2)
    service = m.groups(3)
#    messages = m.groups

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
