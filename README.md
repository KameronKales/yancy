# Summary

I built Yancy as a way to get my feet wet with scikit-learn again. I used it extensively 3+ years ago and had not touched it since.

This project was a super simple implementation. Please feel free to improve the code if you would like. I welcome all pull requests :)

The major learnings I had while developing this were:

- deciding which models to use. I previously used an SVM to classify data years ago. this ended up being ineffective in classifying my data, and I switched to using a linear SVC.

- working with env variables - prior to this, I ashamedly worked with hard coded env variables 90% of the time. this let me learn how to implement in python (I have used env variables in javascript for awhile now)

- standing up postgresql - I have previously used postgresql but had not worked with it in years. I chose to use that as a way to refresh myself.

---

You can run the code after:

- importing the data from the data/spam.csv file
- passing in the following env variables:
  - host
  - dbname
  - user
  - password
  - port

---
