from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import mglearn

iris_dataset = load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)

print("X_train 크기: {} y_train 크기 : {}".format(X_train.shape, y_train.shape))
print("X_test 크기: {} y_test 크기 : {}".format(X_test.shape, y_test.shape))


iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o',
                           hist_kwds={'bins':20}, s=60, alpha=.8, cmap=mglearn.cm3)