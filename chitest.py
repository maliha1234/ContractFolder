import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import LinearSVC
from bioinfokit.analys import stat, get_data
#matplotlib inline
#dataset = pd.read_csv("/Users/malihasarwat/Documents/Summer2020/Sir/FengCodes/Demodata/max_min_all_features_0_2.csv")
#print(dataset.shape)
#print(dataset.head())
df = pd.read_csv("/Users/malihasarwat/Documents/Summer2020/Sir/FengCodes/Demodata/max_min_all_features_0_2.csv")
#df = pd.read_csv("/Users/malihasarwat/Documents/Summer2020/Sir/FeatureList/all_features.csv")
#print(df.head())
df = df.set_index('label')
df = df.drop('name', axis=1)
df = df.head(200)
print(df.head())
res = stat()
res.chisq(df=df)
print(res.summary)
print(res.expected_df)
