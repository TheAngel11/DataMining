import matplotlib.pyplot as plt
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

class Section3:
    def __init__(self, section2):
        self.section2 = section2

    def decomposition_PCA(self):
        pca_modeler = PCA(n_components=3)
        pca_modeler.fit(self.section2.X_train)
        X_train_PCA = pca_modeler.transform(self.section2.X_train)
        print(f"Data X_train_PCA: {X_train_PCA.shape}\n")

        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        for i in range(10):
            ax.scatter(X_train_PCA[self.section2.Y_train == i, 0],
                       X_train_PCA[self.section2.Y_train == i, 1],
                       X_train_PCA[self.section2.Y_train == i, 2], label=i)

        ax.set_xlabel('1st component')
        ax.set_ylabel('2nd component')
        ax.set_zlabel('3rd component')
        ax.legend()

    def decomposition_SVD(self):
        svd_modeler = TruncatedSVD(n_components=3)
        svd_modeler.fit(self.section2.X_train)
        X_train_SVD = svd_modeler.transform(self.section2.X_train)
        print(f"Data X_train_SVD: {X_train_SVD.shape}\n")

        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        for i in range(10):
            ax.scatter(X_train_SVD[self.section2.Y_train == i, 0],
                       X_train_SVD[self.section2.Y_train == i, 1],
                       X_train_SVD[self.section2.Y_train == i, 2], label=i)

        ax.set_xlabel('1st component')
        ax.set_ylabel('2nd component')
        ax.set_zlabel('3rd component')
        ax.legend()

    def descomposition_LDA(self):
        lda_modeler = LinearDiscriminantAnalysis(n_components=3)
        lda_modeler.fit(self.section2.X_train, self.section2.Y_train)
        X_train_LDA = lda_modeler.transform(self.section2.X_train)
        print(f"Data X_train_LDA: {X_train_LDA.shape}\n")

        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        for i in range(10):
            ax.scatter(X_train_LDA[self.section2.Y_train == i, 0],
                       X_train_LDA[self.section2.Y_train == i, 1],
                       X_train_LDA[self.section2.Y_train == i, 2], label=i)

        ax.set_xlabel('1st component')
        ax.set_ylabel('2nd component')
        ax.set_zlabel('3rd component')
        ax.legend()

    def run_all(self):
        self.decomposition_PCA()
        self.decomposition_SVD()
        self.descomposition_LDA()
        plt.show()