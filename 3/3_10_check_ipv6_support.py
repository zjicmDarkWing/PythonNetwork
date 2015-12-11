import socket
import argparse
import netifaces as ni

def inspect_ipv6_support():
    print "IPV6 support build into Python: %s" %socket.has_ipv6
    ipv6_addr = {}
    for interface in ni.interfaces():
        all_address = ni.ifaddresses(interface)
        print "Interface %s:" %interface
        for family,addrs in all_address.iteritems():
            fam_name = ni.address_families[family]
            print "    Address family: %s" %fam_name
            for addr in addrs:
                if fam_name == "AF_INET6":
                    ipv6_addr[interface] = addr["addr"]
                print "        Address: %s" %addr["addr"]
                nmask = addr.get("netmask",None)
                if nmask:
                    print "        Netmask: %s" %nmask
                bcast = addr.get("broadcast",None)
                if bcast:
                    print "        Broadcast: %s" %bcast

    if ipv6_addr:
        print "Found IPV6 address: %s" %ipv6_addr
    else:
        print "No IPV6 interface found!"

if __name__ == '__main__':
    inspect_ipv6_support()
