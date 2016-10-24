
# data[i] is the ith example, its class label is target[i]

import pickle
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection  import train_test_split
from tempfile import TemporaryFile

class Preprocessing:

    def __init__(self):
        self.data = None
        self.target = None

        self.train_data = None
        self.train_target = None

        self.test_data = None
        self.test_target = None

    def process_data(self):
        self.load_file()
        self.shuffle_data()
        self.normalize_data()
        self.split_data()

    def load_file(self):
        with open('forest_data(2.7).pickle', 'rb') as f:
        #Pickle the 'data' dictionary using the highest protocol available.
            self.data = pickle.load(f)
            self.target = pickle.load(f)

    def shuffle_data(self):
        # shuffling the dataset
        reorder = np.arange(len(self.data))
        np.random.shuffle(reorder)
        self.data = self.data[reorder]
        self.target = self.target[reorder]

    def normalize_data(self):
        # identify missing value, then execute normalization
        self.data = preprocessing.normalize(self.data)


#########two approaches for spliting the dataset#########
#option 1: using the train_test_split function from sklearn
    def split_data(self):
        # split dataset in train_data, val_data, and test_data
        data = self.data
        target = self.target
        train_data, test_data, train_target, test_target = train_test_split(data, target, test_size=0.3)
        self.save_data('train.pickle', train_data, train_target)
        test_data, val_data, test_target, val_target = train_test_split(test_data, test_target, test_size=0.5)
        self.save_data('test.pickle', test_data, test_target)
        self.save_data('validate.pickle', val_data, val_target)

#option 2: using the custom function
    def generateDatasets(self):
        l = len(self.data)

        num_70 = math.ceil(l * 0.7)
        num_15_1 = 0
        num_15_2 = 0

        if num_70 < l:
            l = l - num_70
            num_15_1 = math.ceil(l * 0.15)
            if num_15_1 < l:
                l = l - num_15_1
                num_15_2 = l

        # Generate train data
        l = num_70
        print (0,":",l)
        self.train_data = self.data[0:l]
        self.train_data_target = self.target[0:l]
        self.export(self.train_data)
        self.export(self.train_data_target)

        #Generate validation_data
        if num_15_1 != 0:
            self.validation_data = self.data[l:l + num_15_1]
            self.validation_data_target = self.data[l:l + num_15_1]
            print (l, ":", l + num_15_1)
            l = l + num_15_1
            self.export(self.validation_data)
            self.export(self.validation_data_target)

        #Generate test_data
        if num_15_2 != 0:
            self.test_data = self.data[l:l+num_15_2]
            self.test_data_target = self.data [l:l+num_15_2]
            print (l, ":", l+num_15_2)
            l += num_15_2
            self.export(self.test_data)
            self.export(self.test_data_target)

        assert l == len(self.data)

##########end of spliting dataset functions##########

    def save_data(self, filename, data, target):
        with open(filename, 'wb') as f:
            pickle.dump(data, f, 2)
            pickle.dump(target, f, 2)

            
proc =  Preprocessing()
proc.process_data()