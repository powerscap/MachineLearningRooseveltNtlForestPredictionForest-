import pickle
import numpy as np

train_file = open('train.pickle', 'rb')
train_data = pickle.load(train_file)
train_target = pickle.load(train_file)

from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(train_data, train_target) 


test_file = open('test.pickle', 'rb')
test_data = pickle.load(test_file)
test_target = pickle.load(test_file)

test_result = neigh.predict(test_data[0])


print(test_result)
print(test_target[0])