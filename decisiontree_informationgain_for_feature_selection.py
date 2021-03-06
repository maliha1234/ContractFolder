import numpy as np 
import pandas as pd 
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report 
from sklearn.model_selection import KFold
from sklearn import tree
  
# Function importing Dataset 
def importdata(): 
    #balance_data = pd.read_csv('/Users/malihasarwat/Documents/Summer2020/Sir/FengCodes/Demodata/max_min_all_features_0_2.csv') 
    #balance_data = pd.read_csv('/Users/malihasarwat/Documents/Summer2020/Sir/FengCodes/Demodata/max_min_all_features_0_2.csv') 
    #balance_data = pd.read_csv("/Users/malihasarwat/Documents/Summer2020/Sir/FeatureList/max_min_all_features_version_August_27.csv")
    balance_data = pd.read_csv("/Users/malihasarwat/Documents/Summer2020/Sir/DEBO_smartcontract/all_features_with_block_label_sep6.csv")
      
    # Printing the dataswet shape 
    print ("Dataset Length: ", len(balance_data)) 
    print ("Dataset Shape: ", balance_data.shape) 
      
    # Printing the dataset obseravtions 
    print ("Dataset: ",balance_data.head()) 
    return balance_data 
  
# Function to split the dataset 
def splitdataset(balance_data): 
  
    # Separating the target variable 
    X = balance_data.drop('label', axis=1)
    X = X.drop('name', axis=1)
    #X = X.drop('block', axis=1)
    
    #X = X.drop('X2',axis =1)
    #X = X.drop('X14', axis =1)
    #X= X.drop('X15',axis =1)
    X['block'] = X['block'].apply(int, base=16)

    y = balance_data['label']
  
    # Splitting the dataset into train and test 
    #X_train, X_test, y_train, y_test = train_test_split(  
    #X, Y, test_size = 0.2, random_state = 100) 

    X1 = X
    kf = KFold(n_splits=5)
    X = np.array(X)
    y = np.array(y)
    for train_index, test_index in kf.split(X):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
      
    return X, y, X_train, X_test, y_train, y_test 
      
# Function to perform training with giniIndex. 
def train_using_gini(X_train, X_test, y_train): 
  
    # Creating the classifier object 
    clf_gini = DecisionTreeClassifier(criterion = "gini", 
            random_state = 100,max_depth=3, min_samples_leaf=5) 
  
    # Performing training 
    clf_gini.fit(X_train, y_train) 
    print(clf_gini.feature_importances_)
    return clf_gini 
      
# Function to perform training with entropy. 
def tarin_using_entropy(X_train, X_test, y_train): 
  
    # Decision tree with entropy 
    clf_entropy = DecisionTreeClassifier( 
            criterion = "entropy", random_state = 100, 
            max_depth = 3, min_samples_leaf = 5) 
  
    # Performing training 
    clf_entropy.fit(X_train, y_train) 

    dotfile = open("entropy.dot", 'w')
    tree.export_graphviz(clf_entropy, out_file=dotfile)
    dotfile.close()

    print(clf_entropy.feature_importances_)
    return clf_entropy 
  
  
# Function to make predictions 
def prediction(X_test, clf_object): 
  
    # Predicton on test with giniIndex 
    y_pred = clf_object.predict(X_test) 
    print("Predicted values:") 
    print(y_pred) 
    return y_pred 
      
# Function to calculate accuracy 
def cal_accuracy(y_test, y_pred): 
      
    print("Confusion Matrix: ", 
        confusion_matrix(y_test, y_pred)) 
      
    print ("Accuracy : ", 
    accuracy_score(y_test,y_pred)*100) 
      
    print("Report : ", 
    classification_report(y_test, y_pred)) 
  
# Driver code 
def main(): 
      
    # Building Phase 
    data = importdata() 
    X, Y, X_train, X_test, y_train, y_test = splitdataset(data) 
    clf_gini = train_using_gini(X_train, X_test, y_train) 
    clf_entropy = tarin_using_entropy(X_train, X_test, y_train) 
      
    # Operational Phase 
    print("Results Using Gini Index:") 
      
    # Prediction using gini 
    y_pred_gini = prediction(X_test, clf_gini) 
    cal_accuracy(y_test, y_pred_gini) 
      
    print("Results Using Entropy:") 
    # Prediction using entropy 
    y_pred_entropy = prediction(X_test, clf_entropy) 
    cal_accuracy(y_test, y_pred_entropy) 
      
      
# Calling main function 
if __name__=="__main__": 
    main() 