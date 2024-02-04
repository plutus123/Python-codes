import psycopg2 as psg
conn=psg.connect(database='dvdrental',user='postgres',password='vishwas@1')
cur=conn.cursor()
cur.execute('select * from payment')
cur.fetchmany(10)
