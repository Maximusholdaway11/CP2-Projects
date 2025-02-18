#Max Holdaway Movie Recommender

import csv

def get_movie_list():
    list_of_movies = []
    with open("movie_recommender/Movies list.csv") as csv_file:
        next(csv_file)
        csv_file = csv.reader(csv_file)
        for row in csv_file:
            movie = {"title": row[0], "directors": row[1], "genre": row[2], "rating": row[3], "length" : row[4], "actors": row[5]}
            list_of_movies.append(movie)
        return list_of_movies

def print_entire_movie_list(list_of_movies):
    print("")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("")
    if list_of_movies is not []:
        for dict in list_of_movies:
            print("")
            print(f"This is the title of the movie: {dict['title']}, this is the director of the movie: {dict['directors']} this is the genre: {dict['genre']}, this is the rating {dict['rating']}, this is how long the movie is (in minutes): {dict['length']}, these are the notable actors: {dict['actors']}.")
            print("")
            print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

def string_filters(list_of_filtered_movies, name, key):
    key = key.lower()
    matches = []
    if key not in ["title", "directors", "genre", "rating", "actors"]:
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

def main():
    list_of_movies = get_movie_list()
    list_of_filtered_movies = get_movie_list()
    while True:
        print("""1. Print the entire movie list.
2. Do the movies filters
3. Exit""")
        user_decision = input("Please select one of the options (using numbers 1-3): ")
        if user_decision.isnumeric():
            user_decision = int(user_decision)
            if user_decision == 1:
                print("Here is your list of movies:")
                print_entire_movie_list(list_of_movies)
            elif user_decision == 2:
                for x in range(1):
                    user_filter_type = input("Please tell me what you want to filter by first (Title, Directors, Genre, Rating, Actors, Length): ")
                    if user_filter_type == "length":
                        user_length_type = input("Do you want to search for movies that are below an hour, exactly an hour, or above an hour long (don't include long just put something like |below an hour|): ")
                        list_of_filtered_movies = integer_filters(list_of_filtered_movies, user_length_type)
                    else:
                        user_name_search = input("Please tell me the name of what you searching for: ")
                        list_of_filtered_movies = string_filters(list_of_filtered_movies, user_name_search, user_filter_type)
            elif user_decision == 3:
                print("Hope you found the movies you were looking for!")
                break
            else:
                print("You have not selected one of the options please try again.")
        else:
            print("You have not selected a number please try again.")

main()