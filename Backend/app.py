 
from flask import Flask,jsonify
import requests
import pymongo
import json
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

client = pymongo.MongoClient("mongodb://syed:BDat1004@ac-syr02uu-shard-00-00.wcbnerx.mongodb.net:27017,ac-syr02uu-shard-00-01.wcbnerx.mongodb.net:27017,ac-syr02uu-shard-00-02.wcbnerx.mongodb.net:27017/?ssl=true&replicaSet=atlas-lpmvkc-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test
db = client.get_database('Data_file')
records = db.Data_file
df = pd.DataFrame()
df = df.append(list(records.find({})), ignore_index=True)

@app.route('/')
def index():
    return 'API is ON'

@app.route('/getTopLanguage')
def getTopLanguage():
    p=df['original_language'].value_counts()
    l = p[:10].reset_index().values.tolist()
    l.insert(0,['Language','Count of Movies'])
    return jsonify({'values': l})

@app.route('/getTopPopularity')
def getTopPopularity():
    j = df.sort_values(by=['popularity'], ascending=False)
    j = j[:10]['title'].values.tolist()
    return jsonify({'values': j})

@app.route('/getTopVoteCount')
def getTopVoteCount():
    j = df.sort_values(by=['vote_count'], ascending=False)
    j = j[:10]['title'].values.tolist()
    return jsonify({'values': j})

@app.route('/getTopVoteAverage')
def getTopVoteAverage():
    j = df.sort_values(by=['vote_average'], ascending=False)
    j = j[:10]['title'].values.tolist()
    return jsonify({'values': j})

@app.route('/getLeastPopularity')
def getLeastPopularity():
    j = df.sort_values(by=['popularity'], ascending=False)
    j = j[7474:7484]['title'].values.tolist()
    return jsonify({'values': j})

@app.route('/getMovieDetail/<movie>')
def getMovieDetail(movie):
    j = df.loc[df['title'].str.contains(movie, case=False)].drop(columns=['_id', 'poster_path','id','backdrop_path','trailer','genre_ids']).values.tolist()
    j.insert(0,['title', 'overview', 'release_date', 'popularity', 'original_title','vote_count', 'video', 'adult', 'vote_average', 'media_type','original_language'])
    return jsonify({'values': j})

if __name__ == '__main__':
    app.run(debug=True)
    app.run()

