#Max Holdaway Updated Personal Library Program

#Function for adding songs to the library
def add_items(user_library, song_genre, song_name, song_release_date, song_age, song_creator):
    if song_name not in user_library:
        song_dictionary = {"song_genre": song_genre, "song_creator": song_creator, "song_release_date": song_release_date, "song_age": song_age, "song_name": song_name}
        user_library.append(song_dictionary)
    else:
        print("There is already a song in the list with the same name.")
    return user_library

#Function for removing songs from the library
def remove_items(user_library, song_name):
    library_index = search_for_item_index(user_library, song_name)
    if library_index is not None:
        user_library.remove(user_library[library_index])
        print("You have succesfully removed that song.")
        return user_library
    else:
        print("There is no song with that name to remove.")
    

#Function for searching for an songs index in the library
def search_for_item_index(user_library, song_name):
    for item in user_library:
        if item.get('song_name') == song_name:
            return user_library.index(item)

#Function for searching for an song in the library.
def search_for_item_details(user_library, library_index):
    if library_index is not None:
        print(user_library[library_index])
        return user_library[library_index]
    else:
        print("This song is not in the library.")

#Function for updating a songs details
def update_items(user_library, song_name, song_genre=None, song_release_date=None, song_age=None, song_creator=None):
    library_index = search_for_item_index(user_library, song_name)
    if library_index is not None:
        if song_genre is not None:
            user_library[library_index]["song_genre"] = song_genre
        if song_release_date is not None:
            user_library[library_index]["song_release_date"] = song_release_date
        if song_age is not None:
            user_library[library_index]["song_age"] = song_age
        if song_creator is not None:
            user_library[library_index]["song_creator"] = song_creator
        print("You have succesfully updated the information for that song.")
        return user_library
    else:
        print("There is not a song with that name in the library.")

#The main user interface or main function
def main():
    user_library = []

    print("This is a library that stores music.")
    while True:

        user_input = input("""Which tool do you want to use?: 
        1. Add a song
        2. Remove a song
        3. Search for a specific song
        4. Update a songs details
        5. See a list of all the names of songs and who made them
        6. See a list of all the names of songs and their related details
        7. Exit \n""")

        if user_input.isnumeric() is True:
            user_input = int(user_input)

            if user_input == 1:
                user_song_name_add = input("What is the name of the song you want to add?: ")
                user_song_genre = input("What is the name the genre for the music you want to add?: ")
                user_song_release_date = input("When was this song released?: ")
                user_song_age = input("How old is the song?: ")
                user_song_creator = input("Who created the song?: ")
                user_library = add_items(user_library, user_song_genre, user_song_name_add, user_song_release_date, user_song_age, user_song_creator)

            elif user_input == 2:
                user_item_remove = str(input("What do you want to remove?: "))
                if user_library != []:
                    user_library = remove_items(user_library, user_item_remove)
                else:
                    print("You can't remove anything when you don't have anything in the library.")

            elif user_input == 3:
                user_item_search = input("What is the name of the song you are searching for?: ")
                user_library_index = search_for_item_index(user_library, user_item_search)
                if user_library_index is not None:
                    print(f"This is your song's name: {search_for_item_details(user_library, user_library_index)["song_name"]}, this is your songs genre: {search_for_item_details(user_library, user_library_index)["song_genre"]}, this is your song's release date: {search_for_item_details(user_library, user_library_index)["song_release_date"]}, this is your song's age: {search_for_item_details(user_library, user_library_index)["song_age"]}, this is your song's creator: {search_for_item_details(user_library, user_library_index)["song_creator"]}")
                else:
                    print("The song you were looking for is not in the library.")

            elif user_input == 4:
                if user_library != []:
                    user_item_update = input("What is the name of the song you are trying to update info for?: ")
                    user_song_genre_choice = input("Are you going to update the genre of your song?(yes or no): ")
                    if user_song_genre_choice.lower() == "yes":
                        user_song_genre = input("What is the new genre?: ")
                    else:
                        user_song_genre = None
                    user_song_release_date_choice = input("Are you going to update the release date?(yes or no): ")
                    if user_song_release_date_choice.lower() == "yes":
                        user_song_release_date = input("What is the new release date?: ")
                    else:
                        user_song_release_date = None
                    user_song_age_choice = input("Are you going to update how old the song is?(yes or no): ")
                    if user_song_age_choice.lower() == "yes":
                        user_song_age = input("What is the new age for the song?: ")
                    else:
                        user_song_age = None
                    user_song_creator_choice = input("Are you going to update the creator?(yes or no): ")
                    if user_song_creator_choice.lower() == "yes":
                        user_song_creator = input("What is the new creator of the song?: ")
                    else:
                        user_song_creator = None
                    user_library = update_items(user_library, user_item_update, user_song_genre, user_song_release_date, user_song_age, user_song_creator)
                else:
                    print("You can't update a song when you don't have any songs to update.")
            
            elif user_input == 5:
                print("Here are your song creators and names.")
                print("---------------------------------")
                for item1 in user_library:
                    print(f"This is the song creator {item1["song_creator"]}, and its name is {item1["song_name"]}.")
                    print("---------------------------------")
        
            elif user_input == 6:
                print("Here are your song names and details.")
                print("------------------------------------------------------------------------")
                for item2 in user_library:
                    print(f"This is the song's name {item2["song_name"]}, this is the song's genre {item2["song_genre"]}, this is the date the song was released {item2["song_release_date"]}, this is the song's age {item2["song_age"]}, this is the song's creator {item2["song_creator"]}.")
                    print("------------------------------------------------------------------------")

            elif user_input == 7:
                print("Hope this library was useful see you next time.")
                break
        else:
            print("You have not typed in a number please try again.")