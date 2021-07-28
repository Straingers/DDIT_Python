import pymysql

class DaoEmp:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')
        
    def myselect(self):
        ret = []
        curs = self.conn.cursor()
        sql = "select e_id, e_name, birth from emp"
        curs.execute(sql)
         
        rows = curs.fetchall()
        for row in rows:
            ret.append({"e_id" : row[0], "e_name" : row[1], "birth" : row[2]})
            
        return ret
    
    def myinsert(self, e_id, e_name, birth):
        curs = self.conn.cursor()
        sql = f"""
            INSERT INTO emp(e_id, e_name, birth)
            VALUES ('{e_id}', '{e_name}', '{birth}')
        """
        cnt = curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def myupdate(self, e_id, e_name, birth):
        curs = self.conn.cursor()
        sql = f"""
            UPDATE emp
            SET e_name = '{e_name}'
                , birth = '{birth}'
            WHERE e_id = '{e_id}'
        """
        cnt = curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def mydelete(self, e_id):
        curs = self.conn.cursor()
        sql = f"""
            DELETE FROM emp
            WHERE e_id = '{e_id}'
        """
        cnt = curs.execute(sql)
        self.conn.commit()
        return cnt
        
    def __del__(self):
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoEmp()
    