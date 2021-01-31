import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
from sklearn import svm
from sklearn import datasets
import pickle
from joblib import dump, load

# Вывод картинки
# test_data = pd.read_csv('mnist_test.csv', header=None)
# print(test_data)
# image_row = test_data.values[0, 1:]
# print(image_row.shape)
# image_matrix = image_row.reshape(28, 28)
# print(image_matrix)
# plt.imshow(image_matrix, cmap='Greys')
# plt.show()

# Основной блок - Загрузка тестовых и тренировочных образцов
mnist_train = pd.read_csv('mnist_train.csv', header=None)
mnist_test = pd.read_csv('mnist_test.csv', header=None)
cols = ['label']
for i in range(784):
    cols.append('px_{}'.format(i + 1))
mnist_train.columns = cols
mnist_test.columns = cols
train_data = mnist_train.values[:15000, 1:]
test_data = mnist_test.values[:10000, 1:]
train_label = mnist_train.values[:15000, 0]
test_label = mnist_test.values[:10000, 0]
train_data2 = mnist_train.values[15000:30000, 1:]
train_label2 = mnist_train.values[15000:30000, 0]
train_data3 = mnist_train.values[30000:45000, 1:]
train_label3 = mnist_train.values[30000:45000, 0]
train_data4 = mnist_train.values[45000:60000, 1:]
train_label4 = mnist_train.values[45000:60000, 0]

# Проверка системы
test_id = 33
plt.imshow(test_data[test_id, :].reshape(28, 28), cmap='Greys')
plt.show()

# Обучение методом ближайших соседей
# kn_classifier = KNeighborsClassifier(n_jobs=-1)
# kn_classifier = kn_classifier.fit(train_data, train_label)
# Проблемы с памятью при максимальном количестве образцов, т.е. 60000
# print(kn_classifier.predict(test_data[test_id, :].reshape(1, 784)))
# kn_predictions = kn_classifier.predict(test_data)
# print(accuracy_score(test_label, kn_predictions) * 100, '%')

# Обучение нейронной сети
# mlp_classifier = MLPClassifier(verbose=True, tol=0.00001)
# mlp_classifier = mlp_classifier.fit(train_data, train_label)
# print(mlp_classifier.predict(test_data[test_id, :].reshape(1, 784)))
# mlp_predictions = mlp_classifier.predict(test_data)
# print(accuracy_score(test_label, mlp_predictions) * 100, '%')

# Сохранение в файл
# dump(mlp_classifier, 'filename.joblib')

# Загрузка нейронной сети из файла и проверка метрик
a = load('filename.joblib')
a1 = load('filename.joblib')
a1 = a1.partial_fit(train_data2, train_label2)
a1 = a1.partial_fit(train_data3, train_label3)
a1 = a1.partial_fit(train_data4, train_label4)
mlp_predictions = a1.predict(test_data)
print(accuracy_score(test_label, mlp_predictions) * 100, '%')
print(a1.predict(test_data[test_id, :].reshape(1, 784)))
mlp_predictions2 = a.predict(test_data)
print(accuracy_score(test_label, mlp_predictions2) * 100, '%')
print(a.predict(test_data[test_id, :].reshape(1, 784)))
dump(a1, 'filename1.joblib')
