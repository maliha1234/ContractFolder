import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold
import numpy as np
from sklearn.metrics import roc_curve, roc_auc_score, auc
from matplotlib import pyplot as plt
from sklearn.preprocessing import label_binarize
from scipy import interp

#matplotlib inline

#dataset = pd.read_csv("/Users/malihasarwat/Documents/Summer2020/Sir/FengCodes/Demodata/max_min_all_features_0_2.csv")

#this is the CSV file I generated from max min features from mariums dataset all
#dataset = pd.read_csv("/Users/malihasarwat/Documents/Summer2020/Sir/FeatureList/max_min_all_features_version_August_27.csv")

# this dataset is from the block label and features on debo
dataset = pd.read_csv("/Users/malihasarwat/Documents/Summer2020/Sir/DEBO_smartcontract/all_features_with_block_label_sep6.csv")

#print(dataset.shape)
#print(dataset.head())
X = dataset.drop('label', axis=1)
X = X.drop('name', axis=1)
#print(X.head())
X = X.drop('block', axis=1)


#X = X.drop('X2', axis=1)
y = dataset['label']
y = label_binarize(y, classes=[0, 1])
n_classes = y.shape[1]
print(X)
print(y)


kf = KFold(n_splits=7)
X = np.array(X)
y = np.array(y)
for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20,shuffle=False)

classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
y_score = classifier.fit(X_train, y_train).predict(X_test)


false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, y_pred)
roc_auc = auc(false_positive_rate, true_positive_rate)

plt.title('Receiver Operating Characteristic')
plt.plot(false_positive_rate, true_positive_rate, 'b',
label='AUC = %0.2f'% roc_auc)
plt.legend(loc='lower right')
plt.plot([0,1],[0,1],'r--')
plt.xlim([-0.1,1.2])
plt.ylim([-0.1,1.2])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()


