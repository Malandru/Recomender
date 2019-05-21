from sys import argv
import recomend

def test_recomendation():
    movies = 'movies.csv'
    ratings = 'ratings.csv'
    recomend.initFiles(movies, ratings)
    assert type(recomend.recomend('Drama')) == list