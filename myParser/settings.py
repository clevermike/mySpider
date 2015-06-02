#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# -*- author:dongchen -*-

# 解析器的配置设置

# 解析后文件放在myParser/data

PATH = {
    #spider的根目录
    'base': '/home/dongchen/Projects/mySpider/mySpider/mySpider/',
    #数据目录
    'data': '/home/dongchen/Projects/mySpider/mySpider/mySpider/data/',
    #日志目录
    'logs': '/home/dongchen/Projects/mySpider/mySpider/mySpider/logs/',
}

SITE_LIST = [
    'meituan', 'dianping', 'nuomi', 'lashou'
]

MYSQL_CONN = 'mysql://root:123456@localhost:3306/spider?charset=utf8'