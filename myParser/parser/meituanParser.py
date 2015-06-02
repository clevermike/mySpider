#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# -*- author:dongchen -*-

from parser import Parser

from bs4 import BeautifulSoup

class meituanParser(Parser):

    def __init__(self):
        self.site = 'meituan'
        Parser.__init__(self)

    def get_title(self, src):
        return Parser.parse_from_re(src, u'<title>(.+?)</title>')

    def get_description(self, src):
        return Parser.parse_from_re(src, u'<meta name="description" content="(.+?)">')

    def get_bread(self, src):
        soup = BeautifulSoup(src).body
        res = []
        for item in soup.find_all(class_='link--black__green'):
            res.append(item.text.strip())
        return str.join(' > ', res)

    def get_quantity(self, src):
        return Parser.parse_from_re(src, u'<span class="" >已售<span class="deal-component-rating-sold-count hidden orange">([\d]+)</span>')

