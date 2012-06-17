#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

###############################################################################
#                                   License                                   #
###############################################################################
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.

"""
Writes chatlogs in list and dict structures into various formats.
"""

import dateutil.parser
import json

__docformat__ = "restructuredtext en"

def write(chat, outfile, write_format):
    """
    Writes a chat dict to an outfile in the given format.

    :param chat: Dict with chat.
    :type chat: dict
    :param outfile: File to write to.
    :type outfile: file
    :param write_format: Format to write in.
    :type write_format: str
    """
    if write_format == "pidgin":
        format_writer = write_pidgin
    elif write_format == "json":
        format_writer = write_json

    format_writer(chat, outfile)


def write_pidgin(chat, outfile):
    """
    Writes a chat dict as pidgin HTML file.

    :param chat: Dict with chat.
    :type chat: dict
    :param outfile: File to write to.
    :type outfile: file
    """
    # TODO Write correct data into this header.
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


def write_json(chat, outfile):
    """
    Writes a chat dict as JSON file.

    :param chat: Dict with chat.
    :type chat: dict
    :param outfile: File to write to.
    :type outfile: file
    """
    json.dump(chat, outfile, indent=4, sort_keys=True)
    outfile.write("\n")
