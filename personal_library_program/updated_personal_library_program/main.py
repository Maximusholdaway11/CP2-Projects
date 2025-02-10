#Max Holdaway Updated Personal Library Program

#Function for adding items to the library
def add_items(user_library, genre, music_name):
    if music_name not in user_library:
        user_library.append(music_name = dict(gnere = genre, music_name = music_name))
    else:
        print("There is already a song in the list with the same name.")
    return user_library

#Function for removing items from the library
def remove_items(user_library, music_name):
    pass
    

#Function for searching for items in the library
def search_items(user_library, music_name):
    pass

#Function to show all the items in the library
def display_all_items():
    pass

#The main user interface or main function
def main():
    user_library = {}

    print("This is a library that stores music.")
    while True:

        user_input = int(input("""Which tool do you want to use?: 
        1. Add Items
        2. Remove Items
        3. Search For Items
        4. See a list of all items in your library
        5. Exit \n"""))

        if user_input == 1:
            user_genre_add = input("What is the name the genre for the music you want to add?: ")
            user_music_name_add = input("What is the name of the song you want to add?: ")
            add_items(user_library, user_genre_add, user_music_name_add)

        elif user_input == 2:
            user_item_remove = str(input("What do you want to remove?: "))
            remove_items(user_library, user_item_remove)

        elif user_input == 3:
            user_item_search = int(input("Please give me the items order in the list by number (Such as 0, 1, 2, 3, etc...): "))
            search_items(user_library, user_item_search)

        elif user_input == 4:
            print(f"Here is all the items in your library {print(user_library.values())}")
        
        elif user_input == 5:
            print("Hope this library was useful goodbye!")
            break

main()