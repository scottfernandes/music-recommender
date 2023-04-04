from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from sass import *
from flask_cors import CORS
app = Flask(__name__)


CORS(app)


@app.route('/api', methods=['GET','POST'])
def show():

    jso=send_songs()
    search_query = request.args.get('q')
    if not search_query:
        return jsonify([])

    # Filter the dataset based on the search query
    search_results = []
    for item in jso:
        if search_query.lower() in item['name'].lower():
            search_results.append(item)
    return jsonify(jso)





if __name__ == '__main__':
    app.run(debug=True)