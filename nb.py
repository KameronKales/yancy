from __future__ import division
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
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from sklearn.metrics import average_precision_score
spamdata = pd.read_csv("spam.csv")

y = spamdata['v1']
X = spamdata['v2']

cv = TfidfVectorizer(min_df=1,stop_words='english')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= .20, random_state = 4)
x_traincv=cv.fit_transform(X_train)
a=x_traincv.toarray()
x_testcv=cv.transform(X_test)
mnb = MultinomialNB()
y_train=y_train.astype('int')
mnb.fit(x_traincv,y_train)
testmessage=X_test.iloc[0]
predictions=mnb.predict(x_testcv)
print "Here are my predictions", predictions
a=np.array(y_test)
print a
print(average_precision_score(y_test, predictions))
