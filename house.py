"""主文件"""
import os
import sqlite3
from electricity import Electricity
from items import Item
import pinyin

def get_filenames():
    """返回当前目录下数据库文件
        @return list
         文件名列表
    """
    databases = []

    for parent, dirnames, filenames in os.walk('.'):
        for filename in filenames:
            if filename.endswith('.db'):
                databases.append(filename)

    return databases

def main():
    flag = True
    databases = []
    while flag:
        databases = get_filenames()
        if len(databases) == 0:
            print("当前目录下没有数据库文件")
            dbname = input("请输入房屋名：")
            sqlite3.connect(dbname+'.db')
        else:
            print('当前目录下的数据库文件有：')
            for i, database in enumerate(databases):
                print("{0}, {1}".format(i+1, database))
                flag = False

    option = int(input("选择一个地址: "))
    database = databases[option-1]

    func = input('选择一个选项：1.水 2.电 3.气 4.物业 5.网络 6.电视')

    if func == '1':
        water = Item(database, 'Water')
        while True:
            results = water.find_all()
            print("当前的记录为：")
            for result in results:
                print(result)
            opt = input('选择：1.增 2.删 3.改 4.查')
            if opt == '1':
                degree = int(input('请输入当前读数：'))
                recharge= int(input('输入充值数：'))
                fee = float(input('输入费用：'))
                water.add(degree, recharge, fee)


if __name__ == '__main__':
    main()


