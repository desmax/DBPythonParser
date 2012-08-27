#!/usr/bin/python
import os
import re
import MySQLdb
import codecs
from optparse import OptionParser

try:
    parser = OptionParser()
    parser.add_option('-s', '--server',   dest = 'server')
    parser.add_option('-u', '--user',     dest = 'user')
    parser.add_option('-p', '--password', dest = 'password')
    parser.add_option('-d', '--db',       dest = 'db')
    (options, args) = parser.parse_args()

    if options.user:
        user = options.user
    else:
        raise Exception('no mysql user provided')
    if options.password:
        password = options.password
    else:
        raise Exception('no password provided')
    if options.db:
        db = options.db
    else:
        raise Exception('no db provided')
    if options.server:
        server = options.server
    else:
        server = 'localhost'

except Exception as exception:
    print 'Error:', exception, "\nThe End\n"
    exit()


db = MySQLdb.connect(host = server, user = user, passwd = password, db = db)
cur = db.cursor()

dirname = 'mysql'
for item in os.listdir(dirname) :
    try:
        f = codecs.open(os.path.join(dirname, item), 'r', 'utf-8')
        content = f.read()
        pattern = re.compile('INSERT INTO `(.+)` VALUES', re.IGNORECASE)
        match = pattern.match(content)
        if match:
            table_name =  match.group(1)
            try:
                cur.execute("DROP TABLE " + table_name + ";")
                cur.execute("RENAME TABLE " + table_name + "_back TO " + table_name + ";")
            except Exception as exception:
                pass
    except IOError as e:
        pass