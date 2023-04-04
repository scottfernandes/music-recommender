import numpy as np
import pandas as pd
from typing import List, Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
songs = pd.read_csv('flask-server\\songdata.csv')
songs = pd.DataFrame(songs)
songs = songs.sample(n=5000).drop('link', axis=1).reset_index(drop=True)
songs['text'] = songs['text'].str.replace(r'\n', '')
tfidf = TfidfVectorizer(analyzer='word', stop_words='english')
lyrics_matrix = tfidf.fit_transform(songs['text'])
cosine_similarities = cosine_similarity(lyrics_matrix)
similarities = {}
for i in range(len(cosine_similarities)):
    # Now we'll sort each element in cosine_similarities and get the indexes of the songs. 
    similar_indices = cosine_similarities[i].argsort()[:-50:-1] 
    # After that, we'll store in similarities each name of the 50 most similar songs.
    # Except the first one that is the same song.
    similarities[songs['song'].iloc[i]] = [(cosine_similarities[i][x], songs['song'][x], songs['artist'][x]) for x in similar_indices][1:]
class ContentBasedRecommender:
    def __init__(self, matrix):
        self.matrix_similar = matrix

    def _print_message(self, song, recom_song):
        rec_items = len(recom_song)
        
        print(f'The {rec_items} recommended songs for {song} are:')
        for i in range(rec_items):
            print(f"Number {i+1}:")
            print(f"{recom_song[i][1]} by {recom_song[i][2]} with {round(recom_song[i][0], 3)} similarity score") 
            print("--------------------")
        
    def recommend(self, recommendation):
        # Get song to find recommendations for
        song = recommendation['song']
        # Get number of songs to recommend
        number_songs = recommendation['number_songs']
        # Get the number of songs most similars from matrix similarities
        recom_song = self.matrix_similar[song][:number_songs]
        # print each item
        self._print_message(song=song, recom_song=recom_song)
recommedations = ContentBasedRecommender(similarities)
def recommend_song(song):
    n = int(songs[songs['song']==song].index.values[0])
    recommendation = {"song": songs['song'].iloc[n],"number_songs": 5}
    return recommedations.recommend(recommendation)


def send_songs():
    d = {}
    arr=[]
    for x in range(len(songs)):
     i={"id":x,"artist":songs['artist'][x],"song":songs['song'][x],"text":songs['text'][x]}
     arr.append(i)
     '''   po=str(x)
        d[po]={}
        d[po]['id']=x
        d[po]['artist']=songs['artist'][x]
        d[po]['song']=songs['song'][x]
        d[po]['text']=songs['text'][x]'''
    

    return arr