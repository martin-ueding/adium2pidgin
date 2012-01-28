#!/usr/bin/python
# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

# Me
# Other

import dateutil.parser

def write_pidgin(chat, outfile):
    outfile.write('<html><head><meta http-equiv="content-type" content="text/html; charset=UTF-8"><title>Conversation with 307611255 at Mo 01 Aug 2011 10:45:58 CEST on 307259554 (icq)</title></head><body><h3>Conversation with 307611255 at Mo 01 Aug 2011 10:45:58 CEST on 307259554 (icq)</h3>\n')
    for message in chat["messages"]:
        if message["sender"] == chat["account"]:
            color = '#16569E'
        else:
            color = '#A82F2F'

        time = dateutil.parser.parse(message["time"])

        outfile.write(
            '<font color="%(color)s"><font size="2">(%(time)s)</font> <b>%(alias)s:</b></font>%(text)s<br/>\n' %
            {
                "color": color,
                "time": time.strftime("%H:%M:%S"),
                "alias": message["alias"],
                "text": message["text"],
            }
        )
    outfile.write('</body></html>\n')
