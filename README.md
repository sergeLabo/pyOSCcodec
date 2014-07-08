pyOSCcodec
==========

Code and decode OSC Datagram in python 3.4 and beyond.

String are latin-1 encoded and decoded.

This script is a part of :

SimpleOSC:

Copyright (c) Daniel Holth & Clinton McChesney.

pyOSC:

Copyright (c) 2008-2010, Artem Baguinski <artm@v2.nl> et al., Stock,
V2_Lab, Rotterdam, Netherlands.

Streaming support (OSC over TCP):

Copyright (c) 2010 Uli Franke <uli.franke@weiss.ch>, Weiss Engineering,
Uster, Switzerland.

Original Sources at:

https://gitorious.org/pyosc/devel/source/6aaf78b0c1e89942a9c5b1952266791b7ae16012:

Use decodeOSC(data) to convert a binary OSC message data to a Python list.

Use OSCMessage() and OSCBundle() to create OSC message.


### Documentation

See OSCcodec.html in master directory

### Usage

##### Decode

Use decodeOSC(data) to convert a binary OSC message data to a Python list.

##### Create a message

Use OSCMessage() and OSCBundle() to create OSC message.

### Test

Run in terminal

    python3 send_receive.py

### Credits

* Labomedia

### License

pyOSCcodec is released under the GENERAL PUBLIC LICENSE Version 2, June 1991.
See the bundled LICENSE file for details.
