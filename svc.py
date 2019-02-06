import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import preprocessing
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import string
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import average_precision_score
import pickle


spamdata = pd.read_csv("spam.csv")

X = spamdata['v2']
y = spamdata['v1']

cv = TfidfVectorizer(min_df=1,stop_words='english')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state=4)

x_traincv=cv.fit_transform(X_train)
x_testcv=cv.transform(X_test)
y_train=y_train.astype('int')
svclassifier = SVC(kernel='linear')
clf = svclassifier.fit(x_traincv, y_train)
y_pred = svclassifier.predict(x_testcv)
print y_pred
print(average_precision_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
s = pickle.dumps(clf)
brain = pickle.loads(s)

def spam_svc_classifier(spam):
    ## Need to add regex of fuzzing matching for sexual terms we know are bad
    if spam == 'sex' or 'penis':
        return 'True'
    else:
        formatted = cv.transform([spam])
        return brain.predict(formatted)
