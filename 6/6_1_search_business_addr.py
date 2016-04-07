#!/usr/bin/env python
# encoding: utf-8

from pygeocoder import Geocoder


def search_business(business_name):
    results = Geocoder.geocode(business_name)

    for result in results:
        print result


if __name__ == '__main__':
    business_name = "business name"
    print "Searching %s" % business_name
    search_business(business_name)
