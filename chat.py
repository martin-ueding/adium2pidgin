#!/usr/bin/python
# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

class Chat(object):
    def __init__(self, messages):
        """
        Creates a new Chat.

        @param messages: Messages in this chat.
        @type messages: list
        """
        self.messages = messages

class Message(object):
    def __init__(self, time, text, sender, alias):
        """
        @type time: Datetime
        @type text: str
        @type sender: str
        @type alias: str
        """
        self.time = time
        self.text = text
        self.sender = sender
        self.alias = alias
