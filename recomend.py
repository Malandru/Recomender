import pandas as pd
import finder
import sys

movies_file, ratings_file = None, None

def get_csv(filename):
    csv = pd.read_csv(filename)
    csv = csv.set_index('movieId', drop=False)
    return csv

def insert(key, value, dictionary):
    try:
        dictionary[key].append(value)
    except KeyError:
        dictionary[key] = [value]

def get_ratings(matches, csv):
    ratings = {}
    for match in matches:
        try:
            avg = csv.loc[match, "rating avg"]
            evals = csv.loc[match, "evals"]
            if evals > 750:
                insert(avg, match, ratings)
        except KeyError as e: pass
    return ratings

def get_best_rated(ratings):
    rates = list(ratings.keys())
    rates.sort()
    movieIds = []
    for r in rates[:10]:
        movieIds += ratings[r]
    return finder.get_movies(movieIds)

def recomend(pattern):
    global movies_file, ratings_file
    finder.init(movies_file)
    csv = get_csv(ratings_file)
    # Init finder
    matches = finder.get_matches(pattern)
    ratings = get_ratings(matches, csv)
    return get_best_rated(ratings)

def initFiles(moviesFile, ratingsFile):
    global movies_file, ratings_file
    movies_file = moviesFile
    ratings_file = ratingsFile

def main():
    global movies_file, ratings_file
    initFiles(sys.argv[-2], sys.argv[-1])
    pattern = raw_input('Pattern: ')
    finder.init(movies_file)
    csv = get_csv(ratings_file)
    # Init finder
    matches = finder.get_matches(pattern)
    ratings = get_ratings(matches, csv)
    print get_best_rated(ratings)