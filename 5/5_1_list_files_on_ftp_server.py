#!/usr/bin/env python
# encoding: utf-8

import ftplib

FTP_SERVER_URL = "ftp.kernel.org"


def test_ftp_connection(path, username, email):
    ftp = ftplib.FTP(path, username, email)
    ftp.cwd("/pub")
    print "File list at %s:" % path
    files = ftp.dir()
    print files

    ftp.quit()


if __name__ == '__main__':
    test_ftp_connection(FTP_SERVER_URL, "anonymous", "miao@viki.moe")
