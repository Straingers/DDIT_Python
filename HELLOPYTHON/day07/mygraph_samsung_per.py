import pymysql
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def getNames(s_name):
    ret = []
    conn = pymysql.connect(host='localhost', user='root', password='java',
                           db='python', charset='utf8')
    
    curs = conn.cursor()
    sql = """
    SELECT s_name FROM stock 
    GROUP BY s_name
    LIMIT 10
    """
    curs.execute(sql)
    
    rows = curs.fetchall()
    for row in rows:
        ret.append(row[0])
    
    conn.close()
    return np.array(ret)

def getPrices(s_name):
    ret = []
    conn = pymysql.connect(host='localhost', user='root', password='java',
                           db='python', charset='utf8')
    
    curs = conn.cursor()
    sql = """
    SELECT s_price FROM stock WHERE s_name = '{}'
    ORDER BY crawl_date
    """.format(s_name)
    curs.execute(sql)
    rows = curs.fetchall()
    for row in rows:
        ret.append(row[0])
    conn.close()
    return ret

fig = plt.figure()
ax = plt.axes(projection='3d')
z0 = np.array(getPrices('삼성전자'))
z1 = np.array(getPrices('삼성전자우'))
x = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
y = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])

ax.plot3D(x, y, z0, 'maroon')
ax.plot3D(x+1, y, z1, 'blue')
ax.set_title('3D line plot')
plt.show()

if __name__ == '__main__':
    ret = getPrices("삼성전자")
    print(ret)
    