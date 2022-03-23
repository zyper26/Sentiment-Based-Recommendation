from __future__ import division, print_function
import sys
import os
import glob
import re
from model import Recommendation

recommend = Recommendation()

from flask import Flask, request, render_template


# Define a flask app
app = Flask(__name__)


# Main page
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# Prediction page
@app.route('/pred', methods=['POST'])
def search():
    '''
    For rendering results on HTML GUI
    '''
    user_name = str(request.form.get('reviews_username')).lower()
    prediction = recommend.top_5_recommendation(user_name)

    if(not(prediction is None)):
        return render_template('index.html', username=user_name, results=prediction)
    else:
        return render_template("index.html", message="Username doesn't exists. Please enter a valid username.")
        

if __name__ == '__main__':
    app.run(debug=True)