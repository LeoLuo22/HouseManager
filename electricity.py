"""记录电的使用"""
"""需要传入以房屋名称为数据库的文件"""
import sqlite3
from datetime import datetime
from utils.mysqlite import MySqlite

class Electricity():
    def __init__(self, dbpath, table=None):
        """初始化连接到数据库
            @param dbpath
             数据库路径
            @param table
             表名
        """
        self.conn = sqlite3.connect(dbpath)
        if not table:
            self.table = 'Electricity'
        sql = 'create table if not exists Electricity (id INTEGER PRIMARY KEY AUTOINCREMENT, datetime VARCHAR(50), degree INT, recharge INT)'
        self.conn.execute(sql)
        self.cursor = self.conn.cursor()

    def __dict_factory(self, row):
        """将sqlite3查询的返回值转成字典的形式
            @param row
             查询的结果集
        """
        return dict((col[0], row[idx]) for idx, col in enumerate(self.cursor.description))

    def add(self, degree, recharge):
        """添加当前的电表度数
            @param degree
             int,电表读数
            @param recharge
             int, 充值度数
        """
        sql = "INSERT INTO Electricity (datetime, degree, recharge) VALUES ('{0}', {1}, {2})".format(datetime.now(), degree, recharge)
        #print(sql)
        self.conn.execute(sql)
        self.conn.commit()

    def find_all(self):
        """查询所有记录
            @return list
             记录列表
        """
        results = []
        sql = "SELECT * FROM Electricity"
        cursor = self.conn.execute(sql)
        for row in cursor:
            results.append(row)
        return results

    def find_last(self):
        """查询最近一次的记录"""
        sql = "select * from {0} order by id desc limit 0, 1".format(self.table)
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return self.__dict_factory(result)

    def delete(self, ID=None):
        """删除一条记录"""
        sql = "DELETE from Electricity where id = 2"
        self.conn.execute(sql)
        self.conn.commit()

def main():
    electricity = Electricity('金裕青青家园20142.db')
    #electricity.add(50, 0)
    #electricity.delete()
    print(electricity.find_all())

if __name__ == '__main__':
    main()
