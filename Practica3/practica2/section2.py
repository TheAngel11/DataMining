from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import pandas as pd

class Section2:
    def __init__(self, section1):
        self.X_train = None
        self.X_test = None
        self.Y_train = None
        self.Y_test = None
        self.X_train_minmax = None
        self.X_test_minmax = None
        self.X_train_zscore = None
        self.X_test_zscore = None
        self.section1 = section1

    def split_data(self):
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(
            self.section1.X, self.section1.Y, test_size=0.3)

    def normalize_data(self):
        min_max_scaler = preprocessing.MinMaxScaler()
        self.X_train_minmax = min_max_scaler.fit_transform(self.X_train)
        self.X_test_minmax = min_max_scaler.transform(self.X_test)
        zscore_scaler = preprocessing.StandardScaler()
        self.X_train_zscore = zscore_scaler.fit_transform(self.X_train)
        self.X_test_zscore = zscore_scaler.transform(self.X_test)

    def print_data(self):
        print("\nX_train not normalized:")
        print(pd.DataFrame(self.X_train).describe())
        print("X_train minmax:")
        print(pd.DataFrame(self.X_train_minmax).describe())
        print("X_train zscore:")
        print(pd.DataFrame(self.X_train_zscore).describe())
        print("X_test not normalized:")
        print(pd.DataFrame(self.X_test).describe())
        print("X_test minmax:")
        print(pd.DataFrame(self.X_test_minmax).describe())
        print("X_test zscore:")
        print(pd.DataFrame(self.X_test_zscore).describe())


    def run_all(self):
        self.split_data()
        self.normalize_data()
        self.print_data()