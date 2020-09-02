# Load libraries 
from sklearn.datasets import load_iris 
from sklearn.feature_selection import SelectKBest 
from sklearn.feature_selection import chi2 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import LinearSVC
# Load iris data 
iris_dataset = load_iris() 
  
# Create features and target 

#dataset = pd.read_csv("/Users/malihasarwat/Documents/Summer2020/Sir/FengCodes/Demodata/max_min_all_features_0_2.csv")
dataset = pd.read_csv("/Users/malihasarwat/Documents/Summer2020/Sir/FeatureList/max_min_all_features_version_August_27.csv")

#print(dataset.shape)
#print(dataset.head())
X = dataset.drop('label', axis=1)
X = X.drop('name', axis=1)
y = dataset['label']
  
# Convert to categorical data by converting data to integers 
X = X.astype(int) 
  
# Two features with highest chi-squared statistics are selected 
chi2_features = SelectKBest(chi2, k = 10) 
X_kbest_features = chi2_features.fit_transform(X, y) 

chi2score = chi2(X, y)
print(chi2score)
  
# Reduced features 
print('Original feature number:', X.shape[1]) 
print('Reduced feature number:', X_kbest_features.shape[1]) 
print(X_kbest_features)