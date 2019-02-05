import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
ps = PorterStemmer()
stopWords = set(stopwords.words('english'))


spamdata = pd.read_csv("spam.csv")
X = spamdata['v2'][0:100].to_string()

phrases = sent_tokenize(X)
print phrases

#print X[0]
