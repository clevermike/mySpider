#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# -*- author:dongchen -*-

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.dialects.mysql import *
from myParser.settings import MYSQL_CONN

#创建数据库连接,MySQLdb连接方式
mysql_db = create_engine(MYSQL_CONN)

#生成表
metadata = MetaData()

#表的属性描述对象
dealTable = Table(
    "deal", metadata,
    Column('id', INTEGER, primary_key=True),
    Column('identity', VARCHAR(20), unique=True),
    Column('site', VARCHAR(10), nullable=False),
    Column('title', VARCHAR(200), nullable=True),
    Column('description', VARCHAR(200), nullable=True),
    Column('bread', VARCHAR(200), nullable=True),
    Column('cf_auto', INTEGER, nullable=False),
    Column('cf_manual', INTEGER, nullable=False)
)

classifyTable = Table(
    "classify", metadata,
    Column('id', INTEGER, primary_key=True),
    Column('parent', INTEGER, nullable=False),
    Column('name', VARCHAR(50), nullable=False),
)



#创建一个映射类
class Deal(object):
    def __init__(self, identity, site, title, description, bread, quantity):
        """Constructor"""
        self.identity = identity
        self.site = site
        self.title = title
        self.description = description
        self.bread = bread
        self.quantity = quantity
        self.cf_auto = -1
        self.cf_manual = -1

    def __repr__(self):
        return "<Deal('%s', '%s', '%s', '%s', '%s', '%s')>" % \
               (self.identity, self.site, self.title, self.description, self.bread, self.quantity)

class Classify(object):
    def __init__(self, parent, name):
        """Constructor"""
        self.parent = parent
        self.name = name

    def __repr__(self):
        return "<Classify(%d, '%s')>" % (self.parent, self.name)

if __name__ == '__main__':
    metadata.create_all(mysql_db)


#把表映射到类
# mapper(Deal, dealTable)
# mapper(Classify, classifyTable)
#
# Session = sessionmaker(bind=mysql_db)
# session = Session()
# c = Classify(-1, 'haha')
# c.name = 'caonima'
# session.add(c)
# session.commit()

