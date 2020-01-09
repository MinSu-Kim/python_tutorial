from sklearn.datasets import load_iris
iris_dataset = load_iris()

print("iris_dataset의 키:")

[print(key) for key in iris_dataset.keys()]

print(iris_dataset['DESCR'][:193])
print("타깃의 이름 ", iris_dataset['target_names'])
print("특성의 이름 ", iris_dataset['feature_names'])
print("data의 타입 ", type(iris_dataset['data']))
print("data의 크기 ", iris_dataset['data'].shape)
print("data의 처음 다섯 행 :\n", iris_dataset['data'][:5])
