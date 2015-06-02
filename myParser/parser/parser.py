#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# -*- author:dongchen -*-

import os
import re
from settings import PATH


class Parser(object):

    def __init__(self):
        self.path = PATH['data'] + self.site

    def parse(self):
        try:
            file_list = os.listdir(self.path)
        except Exception, e:
            print e
            file_list = []
        res = []
        for f in file_list:
            if '.html' not in f:
                continue
            else:
                src = open(self.path + '/' + f).read()
                item = {
                    'identity': f[:-5],
                    'title': self.get_title(src),
                    'description': self.get_description(src),
                    'bread': self.get_bread(src),
                    'quantity': self.get_quantity(src),
                }
                res.append(item)
        return res

    @staticmethod
    def parse_from_re(src, reg):
        return u'' if len(re.findall(reg, src)) == 0 else re.findall(reg, src)[0].strip()

    def get_title(self, src):
        pass

    def get_description(self, src):
        pass

    def get_bread(self, src):
        pass

    def get_quantity(self, src):
        pass

