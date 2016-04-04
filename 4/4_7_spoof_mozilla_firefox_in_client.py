#!/usr/bin/env python
# coding=utf-8

import urllib2

BROWSER = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"
URL = "http://zjicmisa.org"


def spoof_firefox():
    opener = urllib2.build_opener()
    opener.addheaders = [("User-Agent", BROWSER)]
    result = opener.open(URL)
    print "Response headers:"
    for header in result.headers.headers:
        print "\t", header


if __name__ == '__main__':
    spoof_firefox()
