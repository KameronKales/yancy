import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC
from sklearn import preprocessing
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, make_scorer
import string
import nltk
from sklearn import svm
from nltk.corpus import stopwords
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pickle

spamdata = pd.read_csv("spam.csv")

y = spamdata['v1']
X = spamdata['v2']

le = preprocessing.LabelEncoder()
if X.dtype == object:
    X = le.fit_transform(X)
    X = X.reshape(-1, 1)
else:
    pass


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= .20, random_state = 0)
clf = MultinomialNB().fit(X_train, y_train)
s = pickle.dumps(clf)
clf2 = pickle.loads(s)
print clf2.score(X, y)
spam = ["Kameron Kales was here"]
spam = le.fit_transform(spam)
print spam
print spam.reshape(-1, 1)
print clf2.predict([spam])
