#!/usr/bin/python
import MySQLdb
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

    db = MySQLdb.connect(host = server, user = user, passwd = password, db = db)

except Exception as exception:
    print 'Error:', exception, "\nThe End\n"
    exit()

cur = db.cursor()

cur.execute("SELECT * FROM `table`")

for row in cur.fetchall() :
    print row[1]