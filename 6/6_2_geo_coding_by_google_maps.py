#!/usr/bin/env python
# encoding: utf-8

import argparse
import os
import urllib

ERROR_STRING = "<error>"


def find_lat_long(city):
    url = "http://map.google.com/?q=" + urllib.quote(city) + "&output=js"
    print "Query: %s" % url

    xml = urllib.urlopen(url).read()
    if ERROR_STRING in xml:
        print "\nGoogle cannot interpret the city."
        return
    else:
        lat, lng = 0.0, 0.0
        center = xml[xml.find("{center") + 10:xml.find("}", xml.find("{center"))]
        center = center.replace("lat:", "").replace("lng:", "")
        lat, lng = center.split(",")
        print "Latitude/Logitude: %s/%s\n" % (lat, lng)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="City Geocode Search")
    parser.add_argument("--city", action="store", dest="city", required=True)
    given_args = parser.parse_args()
    city = given_args.city
    print "Finding geographic coordinates of %s" % city
    find_lat_long(city)
