import pymysql
from common.config import conf

class ReadMysqlData(object):

    def __init__(self):
        # 链接数据库
        self.con = pymysql.connect(
            host = conf.get('mysql','host'),
            port=conf.getint('mysql', 'port'),
            user=conf.get('mysql', 'user'),
            password=conf.get('mysql', 'password'),
            database=conf.get('mysql', 'database'),
            charset='utf8')
        # 创建游标
        self.cur = self.con.cursor()

    def find_one(self,sql):
        """获取第一条数据"""
        self.con.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    def find_all(self,sql):
        """获取全部数据"""
        self.con.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def find_count(self,sql):
        # 返回查找到的数据条数
        count = self.cur.execute(sql)
        return count

    def update_data(self, sql):
        """更新语句"""
        try:
            self.cur.execute(sql)
            self.con.commit()
            print("数据库中数据更新成功")
        except Exception as e:
            self.con.rollback()
            print(e)

    def close(self):
        self.cur.close()

readmysql = ReadMysqlData()

if __name__ == '__main__':

    sql = "SELECT * FROM upay_status WHERE payment_no = 'FPP-S-210301-00000816';"
    res = readmysql.find_all(sql)
    print(res)