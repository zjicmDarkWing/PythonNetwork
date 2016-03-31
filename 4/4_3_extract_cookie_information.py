#!/usr/bin/env python
# encoding: utf-8

import cookielib
import urllib
import urllib2

ID_USERNAME = "login_field"
ID_PASSWORD = "password"
USERNAME = "username"
PASSWORD = "password"
LOGIN_URL = "https://github.com/login/"
NORMAL_URL = "https://github.com/"


def extract_cookie_info():
    cj = cookielib.CookieJar()
    login_data = urllib.urlencode({ID_USERNAME: USERNAME,
                                   ID_PASSWORD: PASSWORD})
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    resp = opener.open(LOGIN_URL, login_data)

    for cookie in cj:
        print "First time cookie: %s --> %s" % (cookie.name, cookie.value)
    print "Headers: %s" % resp.headers

    reap = opener.open(NORMAL_URL)
    for cookie in cj:
        print "Second time cookie: %s --> %s" % (cookie.name, cookie.value)
    print "Headers: %s" % resp.headers


if __name__ == '__main__':
    extract_cookie_info()
