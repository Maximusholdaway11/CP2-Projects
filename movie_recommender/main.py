#Max Holdaway Movie Recommender

import csv

def get_movie_list():
    list_of_movies = []
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

def string_filters(list_of_filtered_movies, name, key):
    key = key.lower()
    matches = []
    if key not in ["title", "directors", "genre", "rating", "notable actors"]:
        print(f"You can't search by {key}.")
        return
    for dict_ in list_of_filtered_movies:
        if name in dict_[key]:
            matches.append(dict_)
    return matches

def integer_filters(list_of_filtered_movies, length_range):
    matches = []
    length_range = length_range.lower()
    if length_range == "below an hour":
        for dict_ in list_of_filtered_movies:
            dict_length = dict_['length']
            dict_length = int(dict_length)
            if dict_length < 60:
                matches.append(dict_)
    elif length_range == "exactly an hour":
        for dict_ in list_of_filtered_movies:
            dict_length = dict_['length']
            dict_length = int(dict_length)
            if dict_length == 60:
                matches.append(dict_)
    elif length_range == "above an hour":
        for dict_ in list_of_filtered_movies:
            dict_length = dict_['length']
            dict_length = int(dict_length)
            if dict_length > 60:
                matches.append(dict_)
    else:
        print("You did not select one of the three options.")
    return matches