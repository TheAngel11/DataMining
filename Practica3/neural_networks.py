from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import cross_val_score


class NeuralNetworks:
    def __init__(self, X_train, X_test, Y_train, Y_test):
        self.X_train = X_train
        self.Y_train = Y_train
        self.X_test = X_test
        self.Y_test = Y_test

    def classifier_neural_network(self):
        nn = MLPClassifier(hidden_layer_sizes=(100, 100,), activation='relu', solver='sgd', learning_rate='constant',
                           learning_rate_init=0.02, max_iter=10)
        # Fit the data
        nn.fit(self.X_train, self.Y_train)
        print("Neural Network score: ", nn.score(self.X_test, self.Y_test))

    def ensemble_adaboost(self):
        clf = AdaBoostClassifier(n_estimators=100)
        # Fit the data
        clf.fit(self.X_train, self.Y_train)
        print("\nAdaBoost score: ", cross_val_score(clf, self.X_test, self.Y_test, cv=10))
    def ensemble_bagging(self):
        clf = BaggingClassifier(n_estimators=100)
        # Fit the data
        clf.fit(self.X_train, self.Y_train)
        print("\nBagging score: ", cross_val_score(clf, self.X_test, self.Y_test, cv=10))

    def run_all(self):
        self.classifier_neural_network()
        self.ensemble_adaboost()
        self.ensemble_bagging()
