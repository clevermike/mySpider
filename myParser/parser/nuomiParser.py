#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# -*- author:dongchen -*-

from parser import Parser
from bs4 import BeautifulSoup

class nuomiParser(Parser):

    def __init__(self):
        self.site = 'nuomi'
        Parser.__init__(self)

    def get_title(self, src):
        return Parser.parse_from_re(src, u'<title>(.+?)</title>')

    def get_description(self, src):
        return Parser.parse_from_re(src, u'<meta name="description" content="(.+?)"/>')

    def get_bread(self, src):
        soup = BeautifulSoup(src).body
        res = []
        for item in soup.find_all(class_='crumb '):
            res.append(item.a.text.strip())
        return str.join(' > ', res)

    def get_quantity(self, src):
        return Parser.parse_from_re(src, u'<span class="intro-strong">([\d]+)</span>人已团购</div>')