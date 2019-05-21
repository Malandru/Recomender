import pandas as pd
import sys
import re

data = None, None

def match(pattern, line): # Boolean
    genres = pattern.split(',')
    for gen in genres:
        if gen not in str(line):
            return False
    return True

def get_matches(pattern): # List
    movies = data['movieId']
    genres = data['genres']
    matches = []
    i, lim = 0, len(movies)
    while i < lim:
        if match(pattern, genres[i]):
            matches.append(movies[i])
        i += 1
    return matches

def get_movies(movieIds): # List [str]
    global data
    data = data.set_index('movieId', drop=False)
    titles = []
    for mvId in movieIds:
        movie = data.loc[mvId, 'title']
        if movie != None:
            titles.append(str(movie))
    return titles

def init(file): # Void
    global data
    data = pd.read_csv(file)