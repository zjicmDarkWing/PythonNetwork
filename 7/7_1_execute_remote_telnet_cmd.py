#!/usr/bin/env python
# encoding: utf-8

import getpass
import sys
import telnetlib

HOST = "localhost"


def run_telnet_session():
    user = raw_input("Enter your remote account: ")
    password = getpass.getpass()
    session = telnetlib.Telnet(HOST)
    session.read_until("login: ")
    session.write(user + "\n")
    if password:
        session.read_until("Password: ")
        session.write(password + "\n")
    session.write("ls\n")
    session.write("exit\n")
    print session.read_all()


if __name__ == '__main__':
    run_telnet_session()
