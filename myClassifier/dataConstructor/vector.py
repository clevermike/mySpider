#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# -*- author:dongchen -*-
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

class TfidfVector(object):

    def __init__(self, data, target, test_ratio=0.0):
        self.data = data
        self.target = target
        self.test_ratio = test_ratio
        self.tfidf_vec = TfidfVectorizer()
        self.x_train, self.x_test, self.y_train, self.y_test = \
            train_test_split(self.data, self.target, test_size=self.test_size)
        self.train_vec = self.tfidf_vec.fit_transform(self.x_train).toarray()

    def get_train_vec(self):
        return self.train_vec

    def get_test_vec(self, ):
        return self.tfidf_vec.transform().toarray()


    def get_x(self):
        return self.x_train, self.x_test

    def get_y(self):
        return self.y_train, self.y_test

v = VSM([[0., 0., 0.], [0., .5, 0.], [1., 1., .5]], [2,1,3])
v.tfidf_vec.fit_transform(['美食 青岛']).toarray()

