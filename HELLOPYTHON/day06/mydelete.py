import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')
 
curs = conn.cursor()
 
sql = """delete from hello
         where col01 = %s"""
cnt = curs.execute(sql, 2)
print("cnt", cnt)

conn.commit()

conn.close()