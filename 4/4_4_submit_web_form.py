#!/usr/bin/env python
# coding=utf-8

import requests
import urllib
import urllib2

ID_USERNAME = "username"
ID_EMAIL = "email"
ID_PASSWORD = "password"
USERNAME = "username"
EMAIL = "email"
PASSWORD = "password"
URL = "url"


def submit_form():
    data = {ID_USERNAME: USERNAME,
            ID_EMAIL: EMAIL,
            ID_PASSWORD: PASSWORD,}
    resp = requests.get(URL)
    print "Response to GET request: %s" % resp.content

    resp = requests.post(URL, data)
    print "Headers from a POST request response: %s" % resp.headers


if __name__ == '__main__':
    submit_form()
