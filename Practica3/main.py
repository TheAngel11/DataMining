from practica2.section1 import Section1
from practica2.section2 import Section2
from practica2.section3 import Section3
from practica2.section4 import Section4
from neural_networks import NeuralNetworks
from twenty_newsgroups import TwentyNewsgroups


if __name__ == '__main__':
    section1 = Section1()
    section1.load_data()
    section2 = Section2(section1)
    section2.split_data()
    section2.normalize_data()
    section4 = Section4(section2)
    best_params = section4.KNN()
    print("\nBest params for KNN: ", best_params)
    print()

    neural_networks = NeuralNetworks(section2.X_train, section2.X_test, section2.Y_train, section2.Y_test)
    neural_networks.run_all()

    twenty_newsgroups = TwentyNewsgroups()
    twenty_newsgroups.run_all()
