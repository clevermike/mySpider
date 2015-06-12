#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# -*- author:dongchen -*-

from settings import PATH
import jieba

class WordSpliter(object):

    def __init__(self):
        try:
            self.stopwords = set([line.strip().decode('utf-8') for line in open(PATH['stopwords'])])
        except Exception, e:
            print "fail load stop words list, error:", str(e)
            self.stopwords = set()

    def split_all(self, line):
        line = line.lower()
        words_list = jieba.cut(line, cut_all=True)
        words_list = [w for w in words_list if w not in self.stopwords]
        return words_list

    def split(self, line):
        line = line.lower()
        words_list = jieba.cut(line, cut_all=False)
        words_list = [w for w in words_list if w not in self.stopwords]
        return words_list

    def split_search(self, line):
        line = line.lower()
        words_list = jieba.cut_for_search(line)
        words_list = [w for w in words_list if w not in self.stopwords]
        return words_list

if __name__ == '__main__':
    ws = WordSpliter()

    print "default mode:"
    print ','.join(ws.split('结巴分词是Python语言中效果最好的分词工具，其功能包括结巴分词和Python'))

    print "all mode:"
    print ','.join(ws.split_all('结巴分词是Python语言中效果最好的分词工具，其功能包括结巴分词和Python'))

    print "search mode:"
    print ','.join(ws.split_search('结巴分词是Python语言中效果最好的分词工具，其功能包括结巴分词和Python'))

