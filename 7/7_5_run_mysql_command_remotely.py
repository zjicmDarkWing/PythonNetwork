#!/usr/bin/env python
# encoding: utf-8

from getpass import getpass
from fabric.api import run, env, prompt, cd


def remote_server():
    env.hosts = ["127.0.0.1"]
    env.user = prompt("Enter your system username: ")
    env.password = getpass("Enter your system user password: ")
    env.mysqlhost = "127.0.0.1"
    env.mysqluser = prompt("Enter your db username: ")
    env.mysqlpassword = getpass("Enter your db user password: ")
    env.db_name = ""


def show_dbs():
    q = "show databases"
    run("echo '%s' | mysql -u%s -p%s" % (q, env.mysqluser, env.mysqlpassword))


def run_sql(db_name, query):
    with cd("/tmp"):
        run("echo '%s' | mysql -u%s -p%s -D %s" % (query, env.mysqluser, env.mysqlpassword, db_name))


def create_db():
    if not env.db_name:
        db_name = prompt("Enter the DB name")
    else:
        db_name = env.db_name
    run('echo "CREATE DATABASE %s default character set utf8 collate'
        'utf8_unicode_ci;" | mysql --batch --user=%s --password=%s --host=%s'
        % (db_name, env.mysqluser, env.mysqlpassword, env.mysqlhost), pty=True)


def ls_db():
    if not env.db_name:
        db_name = prompt("Which DB to ls?")
    else:
        db_name = env.db_name
    query = """SELECT table_schema "DB Name",
        Round(Sum(data_length+index_length)/1024/1024,1) "DB Size in MB"
        FROM information_schema.tables
        WHERE table_schema = \"%s\"
        GROUP BY table_schema """ % db_name
    run_sql(db_name, query)


def empty_db():
    db_name = prompt("Enter DB name to empty: ")
    cmd = """
    (echo 'SET foreign_key_checks = 0;'
    (mysqldump -u%s -p%s --add-drop-table --no-data %s |
     grep ^DROP);
     echo 'SET foreign_key_checks = 1;' |
      mysql -u%s -p%s -b %s)
    """ % (env.mysqluser, env.mysqlpassword, db_name,
           env.mysqluser, env.mysqlpassword, db_name)
    run(cmd)


if __name__ == '__main__':
    pass
