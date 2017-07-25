"""水电气等调用"""
import sqlite3
from datetime import datetime

class Item():
    def __init__(self, dbpath, table):
        """初始化Item对象
            @param dbpath
             str, 数据文件路径
            @param table
             str, 指定水电气
        """
        self.conn = sqlite3.connect(dbpath)
        self.table = table
        self.cursor = self.conn.cursor()#查询用
        sql = 'create table if not exists {0} (id INTEGER PRIMARY KEY AUTOINCREMENT, datetime VARCHAR(50), degree INT, recharge INT, fee DOUBLE)'.format(self.table)
        self.conn.execute(sql)

    def __dict_factory(self, row):
        """将sqlite3查询的返回值转成字典的形式
            @param row
             查询的结果集
        """
        return dict((col[0], row[idx]) for idx, col in enumerate(self.cursor.description))

    def add(self, degree, recharge, fee):
        """添加当前的电表度数
            @param degree
             int,电表读数
            @param recharge
             int, 充值度数
            @param fee
             double 充值费用
        """
        sql = "INSERT INTO {0} (datetime, degree, recharge, fee) VALUES ('{1}', {2}, {3}, {4})".format(self.table, datetime.now(), degree, recharge, fee)
        #print(sql)
        self.conn.execute(sql)
        self.conn.commit()

    def find_all(self):
        """查询所有记录
            @return list
             记录列表
        """
        results = []
        sql = "SELECT * FROM {0}".format(self.table)
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
        sql = "DELETE from {)} where id = 2".format(self.table)
        self.conn.execute(sql)
        self.conn.commit()
