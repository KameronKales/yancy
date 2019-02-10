import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import preprocessing
import psycopg2
import psycopg2.extras as e
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import string
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import average_precision_score
import pickle

def connection(sql):
    connection = "host='yancy.c89ytzifs5b6.us-east-1.rds.amazonaws.com' dbname='kam' user='kam' password='Kales333' port='5432'"
    conn = psycopg2.connect(connection)
    cursor = conn.cursor(cursor_factory=e.RealDictCursor)
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return rows

rows = connection("""SELECT * FROM spam_classifier""")
X = []
y = []
for row in rows:
    X.append(row['text'])
    if row['classification'] == 0:
        y.append(0)
    else:
        y.append(1)
cv = TfidfVectorizer(min_df=1,stop_words='english')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state=4)

x_traincv=cv.fit_transform(X_train)
x_testcv=cv.transform(X_test)
svclassifier = SVC(kernel='linear')
clf = svclassifier.fit(x_traincv, y_train)
y_pred = svclassifier.predict(x_testcv)
print(average_precision_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
s = pickle.dumps(clf)
brain = pickle.loads(s)

def spam_svc_classifier(spam):
    ## Need to add regex of fuzzing matching for sexual terms we know are bad
    formatted = cv.transform([spam])
    return brain.predict(formatted)
