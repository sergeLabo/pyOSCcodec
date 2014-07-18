#!/usr/bin/python3
# -*- coding: UTF-8 -*-

## test.py

#############################################################################
# Copyright (C) Labomedia July 2014
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franproplin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#############################################################################

'''
Impossible character:
'Œ', œ, 合久必分, 分久必合
'''

from time import sleep
from send_receive import Send, Receive
from OSCcodec import OSCMessage, decodeOSC

def main():
    buffer_size = 1024

    ip_in = "127.0.0.1"
    port_in = 9000

    ip_out = "127.0.0.1"
    port_out = 9000

    my_receiver = Receive(ip_in, port_in, buffer_size, verbose=True)
    my_sender = Send(verbose=True)

    print("\n\nTest bug unicode\n")
    test = ['éé éé']

    msg = OSCMessage("/test")
    msg.append(1)
    msg.append(test)
    msg.append("ça va")
    msg.append("où été")
    msg.append(1.23)

    my_sender.send_to(msg, (ip_out, port_out))
    sleep(0.01)
    res = my_receiver.listen()
    if res:
        print(res)

    #######################################################################
    type_list = [   1,
                    1.23,
                    "Amour",
                    [1, 2.45, "toto"],
                    2,
                    {"out": 2.24, "in": 4.32}
                    ]
    print("\n\nTest type")
    for test in type_list:
        my_sender.simple_send_to("/test/", test, (ip_out, port_out))
        sleep(0.01)
        res = my_receiver.listen()
        if res:
            print(test, "=", res[2])

    #######################################################################
    print("\n\nTest unicode")
    unicode_list = ['é', 'à', 'é', 'ù', 'î','ê','@','ô','ï','ö','Â',
                    '[', '}', '{', ']', '|', '#', '~', '%', '<', '>',
                     'Ä', 'Ö', 'Ü', 'Ô', 'ë', '.', ',', ';', '/', '*', '+', '-',
                     '0123456789',
                     'abcdefghijklmnopqrstuvwxyz',
                     'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                    'mais enfin', 'é è', '@ é è', 'étù', 'oeuvre',
                    "Ô ! léopard semblables,",
                    "N'ont que l'habit pour tous talents!"
                    ]

    for test in unicode_list:
        my_sender.simple_send_to("/test/", test, (ip_out, port_out))
        sleep(0.01)
        res = my_receiver.listen()
        if res:
            print(test, "=", res[2])

    #######################################################################
    print("\n\nTest bug unicode")
    bug_list = ['éé', 'é ù', 'é é', 'à é', 'ù à',
                "je l'ai emporté à la maison !",
                "tu es un enfoiré",
                '''
    sur un arbre perché,
    c'était un péché (et non pas pêcher).
                ''',
                "à la claire fontaine,\nj'ai chanté tout l'été.",
                "\n",
                "j'ai bien un saut de ligne. fin",
                "dispersée, se recomposera »."
                ]

    for test in bug_list:
        my_sender.simple_send_to("/test/", test, (ip_out, port_out))
        sleep(0.01)
        res = my_receiver.listen()
        if res:
            print(test, "=", res[2])

    #######################################################################

main()
