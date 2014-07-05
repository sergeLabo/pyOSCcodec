pyOSCcodec
==========

Code and decode OSC Datagram in python 3.4 and beyond


This script is a part of :

SimpleOSC:
    Copyright (c) Daniel Holth & Clinton McChesney.
pyOSC:
    Copyright (c) 2008-2010, Artem Baguinski <artm@v2.nl> et al., Stock,
    V2_Lab, Rotterdam, Netherlands.
Streaming support (OSC over TCP):
    Copyright (c) 2010 Uli Franke <uli.franke@weiss.ch>, Weiss Engineering,
    Uster, Switzerland.

Sources at:
https://gitorious.org/pyosc/devel/source/6aaf78b0c1e89942a9c5b1952266791b7ae16012:
and
https://gitorious.org/pyosc/devel/commit/febccde3e36bb158b44f0235dd340ab324aa10a5

#### ChangeLog

2 Mar. 2013
    Added True and False nonstandard type tag

23 June 2014
    Changed 'latin1' to 'utf8'

#### Documentation

wiki

#### Usage

##### Decode

Use decodeOSC(data) to convert a binary OSC message data to a Python list.

##### Create a message

Use OSCMessage() and OSCBundle() to create OSC message.


#### Credits
* Labomedia
