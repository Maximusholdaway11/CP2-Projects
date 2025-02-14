#Max Holdaway Movie Recommender

import csv

list_of_movies = []
list_of_filtered_movies = []

def get_movie_list(list_of_movies):
    with open("movie_recommender/Movies list.csv") as csv_file:
        next(csv_file)
        csv_file = csv.reader(csv_file)
        for row in csv_file:
            movie = {"title": row[0], "directors": row[1], "genre": row[2], "rating": row[3], "length" : row[4], "notable actors": row[5]}
            list_of_movies.append(movie)
        return list_of_movies

def print_entire_movie_list(list_of_movies):
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("")
    if list_of_movies is not []:
        for dict in list_of_movies:
            print("")
            print(f"This is the title of the movie: {dict['title']}, this is the director of the movie: {dict['directors']} this is the genre: {dict['genre']}, this is the rating {dict['rating']}, this is how long the movie is (in minutes): {dict['length']}, these are the notable actors: {dict['notable actors']}.")
            print("")
            print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

def title_filter(list_of_filtered_movies, title):
    title.split(" ")

    for dict in list_of_filtered_movies:
        if dict['title'] in title:
            list_of_filtered_movies.append(dict['title'])
    return list_of_filtered_movies

list_of_movies = get_movie_list(list_of_movies)

list_of_filtered_movies = get_movie_list(list_of_filtered_movies)

list_of_filtered_movies = title_filter(list_of_filtered_movies, "Redemption")
print(list_of_filtered_movies)