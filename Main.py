from flask import Flask, jsonify,request
import csv
import pandas as pd

app = Flask(__name__)

data = pd.read_csv('articles.csv')
data.rename(columns = {'': 'id'},inplace=True)



All_books = []

with open('articles.csv', encoding = 'utf-8') as f:
    reader = csv.reader(f)
    data2 = list(reader)
    All_books = data2[1:]

if __name__=='__main__':
    app.run()
