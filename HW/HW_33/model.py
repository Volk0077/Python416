import pickle
import os


class Movie:
    def __init__(self, title, genre, director, year, duration, studio, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f"{self.title} ({self.year})"
    

class MovieModel:
    def __init__(self):
        self.movies_name = "movies.txt"
        self.movies = self.load_data()

    def add_movie(self, dict_movie):
        movie = Movie(*dict_movie.values())
        self.movies[movie.title] = movie

    def get_all_movies(self):
        return self.movies.values()
    
    def get_single_movie(self, user_title):
        movie = self.movies[user_title]
        dict_movie = {
            "название фильма": movie.title,
            "жанр": movie.genre,
            "режиссер": movie.director,
            "год выпуска": movie.year,
            "длительность": movie.duration,
            "студия": movie.studio,
            "актеры": movie.actors,
        }
        return dict_movie
    
    def remove_movie(self, movie_title):
        return self.movies.pop(movie_title)

    def save_data(self):
        with open(self.movies_name, "wb") as file:
            pickle.dump(self.movies, file)

    def load_data(self):
        if os.path.exists(self.movies_name):
            with open(self.movies_name, "rb") as file:
                return pickle.load(file)
        else:
            return {}