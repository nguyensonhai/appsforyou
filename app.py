from flask import Flask, render_template, session, redirect, request
from bson import ObjectId
from pymongo import MongoClient
app = Flask(__name__)
app.secret_key = "appsforyou"
# uri = ''
# client = MongoClient(uri)
# database = client.appsforyou
# collection_account = database['Account']


@app.route('/', methods=['POST', 'GET'])
def login():
    return render_template('index.html')


@app.route('/landing')
def landing():
   return render_template('landing.html')

@app.route('/generic')
def generic():
   return render_template('generic.html')

@app.route('/elements')
def elements():
   return render_template('elements.html')

if __name__ == '__main__':
    app.run(debug=True)
