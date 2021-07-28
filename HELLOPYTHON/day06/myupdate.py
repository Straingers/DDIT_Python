import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')
 
curs = conn.cursor()
 
sql = """
        update hello
         set col02 = %s
           , col03 = %s
         where col01 = %s
    """
data = ("5", "4", 3)
cnt = curs.execute(sql, data)
print("cnt", cnt)
conn.commit()

conn.close()