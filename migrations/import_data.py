import psycopg2
import psycopg2.extras as e
from flask import Response
import pandas as pd
import sys
from sqlalchemy import create_engine

spamdata = pd.read_csv("migrations/updated_spam.csv")
#print type(spamdata)
X = spamdata['v2']
y = spamdata['v1']
uuid = spamdata['uuid']


engine = create_engine("postgresql+psycopg2://kam:Kales333@yancy.c89ytzifs5b6.us-east-1.rds.amazonaws.com:5432/kam")

def import_data():
    try:
        spamdata.to_sql('spam_classifier', index=True, con = engine, if_exists='append')
        cur = conn.cursor()
        table_name = 'spam_classifier'
        print("Loaded data into {}".format(table_name))
        conn.close()
        print("DB connection closed.")

    except Exception as e:
        print("Error: {}".format(str(e)))
        sys.exit(1)

import_data()
