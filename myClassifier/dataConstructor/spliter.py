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
        words_list = [w for w in words_list if w not in self.stopwords and len(w) > 0]
        return words_list

    def split(self, line):
        line = line.lower()
        words_list = jieba.cut(line, cut_all=False)
        words_list = [w for w in words_list if w not in self.stopwords and len(w) > 0]
        return words_list

    def split_search(self, line):
        line = line.lower()
        words_list = jieba.cut_for_search(line)
        words_list = [w for w in words_list if w not in self.stopwords and len(w) > 0]
        return words_list

    @staticmethod
    def get_words_list(data_set):
        vocab_set = set([])
        for document in data_set:
            vocab_set = vocab_set | set(document)
        return list(vocab_set)

text = u"根据每篇文档中词的个数，我们进行了文档量化的第一个尝试。但对于那些已经学过向量空间模型中“向量”概念的人来说，第一次尝试量化的结果不能进行比较。这是因为它们不在同一词汇空间中。"
if __name__ == '__main__':
    ws = WordSpliter()

    print "default mode:"
    print "','".join(ws.split(text))

    print "all mode:"
    print "','".join(ws.split_all(text))

    print "search mode:"
    print "','".join(ws.split_search(text))

