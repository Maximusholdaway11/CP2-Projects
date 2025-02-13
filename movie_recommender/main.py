#Max Holdaway Movie Recommender

import csv

list_of_movies = []

def get_movie_list(list_of_movies):
    with open("movie_recommender/Movies list.csv") as csv_file:
        next(csv_file)
        csv_file = csv.reader(csv_file)
        for row in csv_file:
            movie = {"title": row[0], "director": row[1], "genre": row[2], "rating": row[3]}
            list_of_movies.append(movie)
        return list_of_movies

helpful_string = "e: Fantasy/Adventure, this is the rating PG-13."



def print_entire_movie_list(list_of_movies):
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("")
    if list_of_movies is not []:
        for dict in list_of_movies:
            print("")
            print(f"This is the title of the movie: {dict['title']}, this is the director of the movie: {dict['director']} this is the genre: {dict['genre']}, this is the rating {dict['rating']}.")
            print("")
            print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

