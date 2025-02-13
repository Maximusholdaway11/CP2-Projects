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

def print_entire_movie_list(list_of_movies):
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("")
    if list_of_movies is not []:
        for dict in list_of_movies:
            print("")
            print(f"This is the title of the movie: {dict['title']}, this is the director of the movie: {dict['director']} this is the genre: {dict['genre']}, this is the rating {dict['rating']}.")
            print("")
            print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

def movie_filters(list_of_movies, genre_decision, genre, rating_decision, rating):
    if genre_decision.lower() == "yes":
        if rating_decision.lower() == "no":
            for dict in list_of_movies:
                if dict['genre'] == genre:
                    print(f"This is the title of the movie: {dict['title']}, this is the director of the movie: {dict['director']} this is the genre: {dict['genre']}, this is the rating {dict['rating']}.")
                    print("")
    elif rating_decision.lower() == "yes":
        if genre_decision.lower() == "no":
            for dict in list_of_movies:
                if dict['rating'] == rating:
                    print(f"This is the title of the movie: {dict['title']}, this is the director of the movie: {dict['director']} this is the genre: {dict['genre']}, this is the rating {dict['rating']}.")
                    print("")
    elif genre_decision.lower() == "yes" and rating_decision.lower() == "yes":
        for dict in list_of_movies:
            if dict['genre'] == genre and dict['rating'] == rating:
                print(f"This is the title of the movie: {dict['title']}, this is the director of the movie: {dict['director']} this is the genre: {dict['genre']}, this is the rating {dict['rating']}.")
                print("")
    else:
        print("Unexpected error using filters please try again.")

list_of_movies = get_movie_list(list_of_movies)

print_entire_movie_list(list_of_movies)

movie_filters(list_of_movies, "yes", "Drama", "no", "R")