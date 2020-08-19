import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import LinearSVC
#matplotlib inline
dataset = pd.read_csv("/Users/malihasarwat/Documents/Summer2020/Sir/FengCodes/Demodata/max_min_all_features_0_2.csv")
#print(dataset.shape)
#print(dataset.head())
X = dataset.drop('label', axis=1)
X = X.drop('name', axis=1)
y = dataset['label']

print(X)
print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

classifier = LinearSVC()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))