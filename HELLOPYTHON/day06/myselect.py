import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')
 
curs = conn.cursor()
 
sql = "select col01, col02, col03 from hello"
curs.execute(sql)
 
rows = curs.fetchall()

for row in rows:
    print(row)

conn.close()