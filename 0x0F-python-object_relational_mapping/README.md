<h1>0x0F. Python - Object-relational mapping</h1>
<h3></h3>Description</h3>
<p></p>The goal of this project is to learn how to use an Object-relational mapper (ORM). The module MySQLdb will be used in Python to connect to a MySQL database, and then the module SQLAlchemy will be used.</p>

<h3>Background Context</h3>
<p>In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.</p>

<strong>Without ORM:</strong>

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
With an ORM:

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)
session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
<h3>Resources</h3>
<li>Object-relational mappers</li>

<li>mysqlclient/MySQLdb documentation (please don’t pay attention to _mysql)</li>

<li>MySQLdb tutorial</li>

<li>SQLAlchemy tutorial</li>li>

<li>SQLAlchemy</li>

<li>mysqlclient/MySQLdb</li>

<li>Introduction to SQLAlchemy</li>

<li>Flask SQLAlchemy</li>

<li>10 common stumbling blocks for SQLAlchemy newbies</li>li>

<li>Python SQLAlchemy Cheatsheet</li>

<li>SQLAlchemy ORM Tutorial for Python Developers (Warning: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)</li>

<li>SQLAlchemy Tutorial</li>

<h3>Table of contents</h3>
Files	Description
0-select_states.py	Python script that lists all states from the database hbtn_0e_0_usa
1-filter_states.py	Python script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
2-my_filter_states.py	Python script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument
3-my_safe_filter_states.py	Python script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument safe from SQL injections
4-cities_by_state.py	Python script that lists all cities from the database hbtn_0e_4_usa
$ sudo pip3 install mysqlclient	
...	
$ python3	
import MySQLdb MySQLdb.version_info (2, 0, 3, 'final', 0)

Install SQLAlchemy module version 1.4.x
$ sudo pip3 install SQLAlchemy ... $ python3

import sqlalchemy sqlalchemy.version '1.4.22'

Also, you can have this warning message:
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re moved in a future release.")
cursor.execute(statement, parameters)

You can ignore it. 
