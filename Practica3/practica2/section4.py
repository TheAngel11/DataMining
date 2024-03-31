from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import GridSearchCV
import numpy as np
import matplotlib.pyplot as plt


class Section4:
    def __init__(self, section2):
        self.section2 = section2

    def compute_test(self, X, Y, clf, cv=10):
        kf = KFold(n_splits=cv)
        kf.get_n_splits(X)
        scores = []

        for i, (train_index, test_index) in enumerate(kf.split(X)):
            X_train, Y_train = X[train_index], Y[train_index]
            X_test, Y_test = X[test_index], Y[test_index]

            clf.fit(X_train, Y_train)
            scores += [accuracy_score(clf.predict(X_test), Y_test)]

        return np.mean(scores)

    def compute_test_extended(self, X, Y, clf, scaler, decomposer, cv=10):
        global X_train, X_test, Y_train, Y_test
        kf = KFold(n_splits=cv)
        kf.get_n_splits(X)
        scores = []

        for i, (train_index, test_index) in enumerate(kf.split(X)):
            X_train, Y_train = X[train_index], Y[train_index]
            X_test, Y_test = X[test_index], Y[test_index]

            x_train_scaled = scaler.fit_transform(X_train) if scaler else X_train

            if type(decomposer) == LinearDiscriminantAnalysis:
                x_train_reduced = decomposer.fit_transform(x_train_scaled, Y_train)
            else:
                x_train_reduced = decomposer.fit_transform(x_train_scaled) if decomposer else x_train_scaled

            x_test_scaled = scaler.transform(X_test) if scaler else X_test
            x_test_reduced = decomposer.transform(x_test_scaled) if decomposer else x_test_scaled

            clf.fit(x_train_reduced, Y_train)
            scores += [accuracy_score(clf.predict(x_test_reduced), Y_test)]

        return np.mean(scores)

    def KNN(self):
        neighbors = np.arange(20) + 1
        parameters = {'n_neighbors': neighbors}
        accuracy = []
        best_parameters = []
        k_nearest = KNeighborsClassifier(n_neighbors=neighbors)
        model = GridSearchCV(k_nearest, parameters, cv=10)
        model = model.fit(self.section2.X_train, self.section2.Y_train)
        predicted_y = model.predict(self.section2.X_test)


        for i in range(2, 15):
            decomposer = TruncatedSVD(n_components=i)
            decomposer.fit(self.section2.X_train)
            X_train_decomposer = decomposer.transform(self.section2.X_train)
            X_test_decomposer = decomposer.transform(self.section2.X_test)
            model = model.fit(X_train_decomposer, self.section2.Y_train)
            accuracy.append(self.compute_test_extended(X_test_decomposer, self.section2.Y_test, model, None, decomposer, 10))
            best_parameters.append(model.best_params_['n_neighbors'])
            print("Best neighbor for Components = " + str(i) + ": " + str(model.best_params_['n_neighbors'])
                  + " with accuracy: " + model.best_score_.__str__())

        plt.figure()
        plt.plot(accuracy)
        plt.xlabel('Number of components')
        plt.ylabel('Accuracy')
        plt.title('KNN - SVD')
        plt.show()

        return best_parameters

    def run_all(self):
        X = self.section2.section1.X
        Y = self.section2.section1.Y
        print("Accuracy without scaling and decomposition: ")
        print(self.compute_test_extended(X, Y, KNeighborsClassifier(n_neighbors=2), None, None, 10))
        print("Accuracy with Z-score: ")
        print(self.compute_test_extended(X, Y, KNeighborsClassifier(n_neighbors=2), preprocessing.StandardScaler(),
                                            None, 10))
        print("Accuracy with PCA: ")
        print(self.compute_test_extended(X, Y, KNeighborsClassifier(n_neighbors=2), None, PCA(n_components=2), 10))
        print("Accuracy with Z-score and PCA: ")
        print(self.compute_test_extended(X, Y, KNeighborsClassifier(n_neighbors=2), preprocessing.StandardScaler(),
                                            PCA(n_components=2), 10))
        print("Accuracy with SVD: ")
        print(self.compute_test_extended(X, Y, KNeighborsClassifier(n_neighbors=2), None, TruncatedSVD(n_components=2),
                                            10))
        print("Accuracy with Z-score and SVD: ")
        print(self.compute_test_extended(X, Y, KNeighborsClassifier(n_neighbors=2), preprocessing.StandardScaler(),
                                            TruncatedSVD(n_components=2), 10))
        print("Accuracy with LDA: ")
        print(self.compute_test_extended(X, Y, KNeighborsClassifier(n_neighbors=2), None,
                                         LinearDiscriminantAnalysis(), 10))
        print("Accuracy with Z-score and LDA: ")
        print(self.compute_test_extended(X, Y, KNeighborsClassifier(n_neighbors=2), preprocessing.StandardScaler(),
                                         LinearDiscriminantAnalysis(), 10))
        print()
        self.KNN()