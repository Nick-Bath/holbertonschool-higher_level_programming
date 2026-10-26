import MySQLdb

def list_all_states(username, password, name):
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=name)

    cur = db.cursor()

    cur.execute("SELECT * from states order by states.id")
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
