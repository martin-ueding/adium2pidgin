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

    def toDict(self):
        return {
            "messages": [message.toDict() for message in self.messages],
        }

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

    def toDict(self):
        return {
            "time": str(self.time),
            "text": self.text,
            "sender": self.sender,
            "alias": self.alias,
        }

