from sklearn.datasets import fetch_20newsgroups
from pprint import pprint
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

class TwentyNewsgroups:
    def __init__(self):
        self.train = None
        self.test = None
        self.train_vectors = None
        self.test_vectors = None

    def load_data(self):
        self.train = fetch_20newsgroups(subset='train')
        self.test = fetch_20newsgroups(subset='test')

    def analyze_data(self):
        print(f"\nData X, Y: {self.train.filenames.shape}, {self.test.filenames.shape}\n")
        print("Target names example: ")
        pprint(self.train.target_names)
        print()
    def text_to_vector(self):
        vectorizer = TfidfVectorizer()
        self.train_vectors = vectorizer.fit_transform(self.train.data)
        self.test_vectors = vectorizer.transform(self.test.data)
        print(f"Train vectors shape: {self.train_vectors.shape}\n")
        print(f"Test vectors shape: {self.test_vectors.shape}\n")

    def multinomial_classifier(self):
        clf = MultinomialNB(alpha=.01)
        clf.fit(self.train_vectors, self.train.target)
        pred = clf.predict(self.test_vectors)
        score = accuracy_score(self.test.target, pred)
        print(f"Accuracy Multinomial: {score}\n")

    def neighbors_classifier(self):
        clf = KNeighborsClassifier()
        clf.fit(self.train_vectors, self.train.target)
        pred = clf.predict(self.test_vectors)
        score = accuracy_score(self.test.target, pred)
        print(f"Accuracy Neighbors: {score}\n")


    def run_all(self):
        self.load_data()
        self.analyze_data()
        self.text_to_vector()
        self.multinomial_classifier()
        self.neighbors_classifier()


