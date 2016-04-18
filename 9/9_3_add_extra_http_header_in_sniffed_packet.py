#!/usr/bin/env python
# encoding: utf-8

from scapy.all import *


def modify_packet_header(pkt):
    if pkt.haslayer(TCP) and pkt.getlayer(TCP).dport == 80 and pkt.haslayer(Raw):
        hdr = pkt[TCP].payload.__dict__
        extra_item = {'Extra Header': ' extra value'}
        hdr.update(extra_item)
        send_hdr = '\r\n'.join(hdr)
        pkt[TCP].payload = send_hdr

        pkt.show()

        del pkt[IP].chksum
        send(pkt)


if __name__ == '__main__':
    sniff(filter="tcp and ( port 80 )", prn=modify_packet_header)
