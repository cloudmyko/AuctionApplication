import sqlite3 as sqlite

conn = sqlite.connect('auctionhouse.db')
curs = conn.cursor()

sql = ''

curs.execute(sql)

conn.commit()

curs.close()