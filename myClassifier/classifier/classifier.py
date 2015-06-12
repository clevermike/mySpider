#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# -*- author:dongchen -*-

from sklearn.neighbors import NearestNeighbors
from predictor import Predictor


class KnnClassifier(object):

    def __init__(self, data_train, data_test, k_neighbors=1):
        self.data_train = data_train
        self.data_test = data_test
        self.k_neighbors = k_neighbors

    def train(self):
        pass


samples = [[0., 0., 0.], [0., .5, 0.], [1., 1., .5]]
y = [2,1,3]
from sklearn.neighbors import NearestNeighbors
neighbors = 3
neigh = NearestNeighbors(n_neighbors=neighbors)
neigh.fit(samples)
NearestNeighbors(algorithm='auto', leaf_size=1)

# algorithm : {‘auto’, ‘ball_tree’, ‘kd_tree’, ‘brute’}, optional
#
#     Algorithm used to compute the nearest neighbors:
#
#         ‘ball_tree’ will use BallTree
#         ‘kd_tree’ will use KDTree
#         ‘brute’ will use a brute-force search.
#         ‘auto’ will attempt to decide the most appropriate algorithm based on the values passed to fit method.
#
for i in range(0,neighbors):
    print neigh.kneighbors([1., 1., 1.])[0][0][i]
    print neigh.kneighbors([1., 1., 1.])[1][0][i]

print Predictor.predict(3, neigh.kneighbors([1., 1., 1.]), y)
