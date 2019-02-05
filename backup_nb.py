import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import preprocessing
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import string
import nltk


spamdata = pd.read_csv("spam.csv")

X = spamdata['v2']
y = spamdata['v1']

le = preprocessing.LabelEncoder()
if X.dtype == object:
    X = le.fit_transform(X)
    print type(X)
    X = X.reshape(-1, 1)
else:
    pass

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

svclassifier = SVC(kernel='linear')
svclassifier.fit(X_train, y_train)
y_pred = svclassifier.predict(X_test)
print y_pred
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
