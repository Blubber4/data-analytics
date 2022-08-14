# A program to show an example of training a KNN algorithm to distinguish images of numbers
#
# @author McMillian, Caleb
# @assignment CSCI 333 Project
# @date 8/9/2022
#

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

if __name__ == '__main__':
    digits = load_digits()

    # part A
    im = digits.images[35]
    print(im)

    # part B
    plt.imshow(im)
    plt.show()

    # part C & D
    x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, random_state=11, test_size=0.70)
    print("Number of training samples:", x_train.shape[0])
    print("Number of testing samples:", x_test.shape[0])

    # part E
    knn = KNeighborsClassifier()
    knn.fit(X=x_train, y=y_train)
    predicted = knn.predict(X=x_test)
    expected = y_test

    wrong = []
    for (p, e) in zip(predicted, expected):
        if p != e:
            wrong.append((p, e))

    print(wrong)
    print("Model accuracy: %.2f%%" % (knn.score(x_test, y_test)*100))
