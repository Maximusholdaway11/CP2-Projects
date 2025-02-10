#Max Holdaway Updated Personal Library Program

#Function for adding items to the library
def add_items(user_library, genre, music_name, song_release_date, song_age, song_creator):
    if music_name not in user_library:
        user_library.append(music_name = dict(genre = genre, song_creator = song_creator, song_release_date = song_release_date, song_age = song_age))
    else:
        print("There is already a song in the list with the same name.")
    return user_library

#Function for removing items from the library
def remove_items(user_library, music_name):
    library_index = search_for_item_index(user_library, music_name)
    if library_index is not None:
        user_library = user_library[library_index].remove()
        print("You have succesfully removed that song.")
    else:
        print("There is no song with that name to remove.")
    

#Function for searching for items in the library
def search_for_item_index(user_library, music_name):
    pass

def search_for_item(user_library, music_name):
    pass

def update_items(user_library, music_name, genre=None, song_release_date=None, song_age=None, song_creator=None):
    library_index = search_for_item_index(user_library, music_name)
    if library_index is not None:
        if genre is not None:
            user_library[library_index["genre"]] = genre
        if song_release_date is not None:
            user_library[library_index["song_release_date"]] = song_release_date
        if song_age is not None:
            user_library[library_index["song_age"]] = song_age
        if song_creator is not None:
            user_library[library_index["song_creator"]] = song_creator
        print("You have succesfully updated the information for that song.")
        return user_library
    else:
        print("There is not a song with that name in the library.")

#Function to show all the items in the library
def display_all_items():
    pass

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

        if user_input == 1:
            user_music_name_add = input("What is the name of the song you want to add?: ")
            user_genre = input("What is the name the genre for the music you want to add?: ")
            user_song_release_date = input("When was this song released?: ")
            user_song_age = input("How old is the song?: ")
            add_items(user_library, user_genre, user_music_name_add, user_song_release_date, user_song_age)

        elif user_input == 2:
            user_item_remove = str(input("What do you want to remove?: "))
            remove_items(user_library, user_item_remove)

        elif user_input == 3:
            user_item_search = input("What is the name of the song you are searching for?: ")
            search_for_item(user_library, user_item_search)

        elif user_input == 4:
            user_item_update = input("What is the name of the song you are trying to update info for?: ")
            update_items()

        elif user_input == 5:
            pass
        
        elif user_input == 6:
            pass

        elif user_input == 7:
            print("Hope this library was useful goodbye!")
            break

main()