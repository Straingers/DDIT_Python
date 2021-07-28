import pymysql
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def getPrices(s_name):
    ret = []
    conn = pymysql.connect(host='localhost', user='root', password='java',
                           db='python', charset='utf8')
    
    curs = conn.cursor()
    sql = """
    SELECT s_price FROM stock WHERE s_name = '{}'
    ORDER BY crawl_date
    """.format(s_name)
    
    print(sql)
    
    curs.execute(sql)
    
    rows = curs.fetchall()
    for row in rows:
        ret.append(row[0])
    
    conn.close()
    return np.array(ret)

def getNames():
    ret = []
    conn = pymysql.connect(host='localhost', user='root', password='java',
                           db='python', charset='utf8')
    
    curs = conn.cursor()
    sql = """ select s_name from stock
        group by s_name """
    
    print(sql)
    
    curs.execute(sql)
    
    rows = curs.fetchall()
    for row in rows:
        ret.append(row[0])
    
    conn.close()
    return np.array(ret)
   
arr_name = getNames()
print(arr_name) 

arrz = []
arrz.append(getPrices(arr_name[0]))
arrz.append(getPrices(arr_name[1]))

arr_per_z = []
imsi0 = (arrz[0]/arrz[0][0])*100
arr_per_z.append(imsi0)
imsi1 = (arrz[1]/arrz[1][0])*100
arr_per_z.append(imsi1)

fig = plt.figure()
ax = plt.axes(projection='3d')

x = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
y = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])

ax.plot3D(x, y, arr_per_z[0], 'maroon')
ax.plot3D(x+1, y, arr_per_z[1], 'blue')
ax.set_title('3D line plot')
plt.show()

if __name__ == '__main__':
    ret = getPrices("삼성전자")
    print(ret)
          