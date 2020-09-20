import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold
import numpy as np

#matplotlib inline

#dataset = pd.read_csv("/Users/malihasarwat/Documents/Summer2020/Sir/FengCodes/Demodata/max_min_all_features_0_2.csv")

#this is the CSV file I generated from max min features from mariums dataset all
#dataset = pd.read_csv("/Users/malihasarwat/Documents/Summer2020/Sir/FeatureList/max_min_all_features_version_August_27.csv")

# this dataset is from the block label and features on debo
dataset = pd.read_csv("/Users/malihasarwat/Documents/Summer2020/Sir/DEBO_smartcontract/all_features_with_block_label_sep6.csv")

#print(dataset.columns[(dataset == 0).all()])
#print(dataset.shape)
#print(dataset.head())
X = dataset.drop('label', axis=1)
X = X.drop('name', axis=1)
#X = X.drop('X2',axis =1)
#X = X.drop('X14', axis =1)
#X= X.drop('X15',axis =1)
#print(X.head())
X['block'] = X['block'].apply(int, base=16)
#X = X.drop('block', axis=1)


#X = X.drop('X2', axis=1)
y = dataset['label']

print(X)
print(y)

X1 = X
kf = KFold(n_splits=5)
X = np.array(X)
y = np.array(y)
for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20,shuffle=False)

classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

print(classifier.feature_importances_)

dotfile = open("dt.dot", 'w')
tree.export_graphviz(classifier, out_file=dotfile)
dotfile.close()



