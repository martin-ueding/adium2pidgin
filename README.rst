.. Copyright © 2012-2014, 2016-2017 Martin Ueding <dev@martin-ueding.de>

############
adium2pidgin
############

In case you have some chat logs from the Mac OS X chat client *Adium* that you
want to convert into format of the multi platform *Pidgin* client, this tool
might be handy for you.

This project was started since the original log reader `cannot read the Adium
logs any more <http://developer.pidgin.im/ticket/4151>`_

Supported Formats
=================

Parser
------

-  Adium XML
-  JSON

Writer
------

-  Purple HTML
-  JSON

How It Works
============

The program usually takes *Adium* style data, which looks like that:

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" ?>
    <chat xmlns="http://purl.org/net/ulf/ns/0.4-02" account="example@example.org" service="Facebook">
    <event type="windowOpened" sender="example@example.org" time="2010-04-02T11:33:51+02:00"></event>
    <message sender="example@example.org" time="2010-04-02T11:33:51+02:00" alias="Me"><div>xxxxxxxxxxxxxxxxxxxx</div></message>
    <message sender="example@example.org" time="2010-04-02T11:35:39+02:00" alias="Me"><div>xxxxxxxxxxxxxxxxxxxxxxxxxx</div></message>
    <message sender="123456789" time="2010-04-02T11:36:04+02:00" alias="other guy"><div><span style="font-family: Helvetica; font-size: 12pt;">xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx</span></div></message>
    <event type="windowOpened" sender="example@example.org" time="2010-04-02T12:02:55+02:00"></event>
    <message sender="123456789" time="2010-04-02T12:02:53+02:00" alias="other guy"><div><span style="font-family: Helvetica; font-size: 12pt;">xxx</span></div></message>
    <event type="windowClosed" sender="example@example.org" time="2010-04-02T12:02:58+02:00"></event></chat>

The logs are parsed into an intermediate structure of lists and dictionaries,
so it can be saved as a simple JSON file to be reimported later on.

.. code-block:: javascript

    {
        "account": "example@example.org",
        "messages": [
            {
                "alias": "Me",
                "sender": "example@example.org",
                "text": "xxxxxxxxxxxxxxxxxxxx",
                "time": "2010-04-02T11:33:51+02:00"
            },
            {
                "alias": "Me",
                "sender": "example@example.org",
                "text": "xxxxxxxxxxxxxxxxxxxxxxxxxx",
                "time": "2010-04-02T11:35:39+02:00"
            },
            {
                "alias": "other guy",
                "sender": "123456789",
                "text": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "time": "2010-04-02T11:36:04+02:00"
            },
            {
                "alias": "other guy",
                "sender": "123456789",
                "text": "xxx",
                "time": "2010-04-02T12:02:53+02:00"
            }
        ],
        "service": "Facebook"
    }

The JSON interface allows conversion between all logs formats, one just needs
to write a parser from a specific format to JSON or a writer from JSON into
some format.

Then this is written to the *Pidgin* HTML format, which looks like that:

.. code-block:: html

    <html><head><meta http-equiv="content-type" content="text/html; charset=UTF-8"><title>Conversation with 307611255 at Mo 01 Aug 2011 10:45:58 CEST on 307259554 (icq)</title></head><body><h3>Conversation with 307611255 at Mo 01 Aug 2011 10:45:58 CEST on 307259554 (icq)</h3>
    <font color="#16569E"><font size="2">(11:33:51)</font> <b>Me:</b></font>xxxxxxxxxxxxxxxxxxxx<br/>
    <font color="#16569E"><font size="2">(11:35:39)</font> <b>Me:</b></font>xxxxxxxxxxxxxxxxxxxxxxxxxx<br/>
    <font color="#A82F2F"><font size="2">(11:36:04)</font> <b>other guy:</b></font>xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx<br/>
    <font color="#A82F2F"><font size="2">(12:02:53)</font> <b>other guy:</b></font>xxx<br/>
    </body></html>

With that intermediate step, adding a new format is as easy as to write a
parser or writer for it.

Installation
============

For all users::

    sudo python setup.py install

Or for yourself::

    python setup.py install --user

Usage
=====

See the manual_ for more usage information.

.. _manual: adium2pidgin.1.rst
