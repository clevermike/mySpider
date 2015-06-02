#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# -*- author:dongchen -*-

from parser import Parser

class dianpingParser(Parser):

    def __init__(self):
        self.site = 'dianping'
        Parser.__init__(self)

    def get_title(self, src):
        return Parser.parse_from_re(src, u'<title>(.+?)</title>')

    def get_description(self, src):
        return Parser.parse_from_re(src, u'<meta name="Description" content="(.+?)"/>')

    def get_bread(self, src):
        return u''

    def get_quantity(self, src):
        return Parser.parse_from_re(src, u'<span>已售<em class="J_current_join">([\d]+)</em>份</span>')

