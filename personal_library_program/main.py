#Max Holdaway Personal Library Program

#Function for adding items to the library
def AddItems(List, Item1):
    List.append(Item1)
    print(f"You have succesfully added {Item1} to the list.")
    return List

#Function for removing items from the library
def RemoveItems(List, Item2):
    List.remove(Item2)
    print(f"You have succesfully removed {Item2} from the list.")
    return List

#Function for searching for items in the library
def SearchItems(List, Item3):
    List = tuple(List)
    print(f"Here is what you were searching for: {List[Item3]}")

#The main user interface or main function
def main():
    #Making the list for the library
    LibraryList = []

    #Getting the users type of library in case they need a reminder of what they need to put into this
    UserTypeOfLibrary = str(input("What is this library going to store? (Like is it music, movies, etc...): "))
    while True:

        #Asking which tool the user wants to use
        UserInput = int(input("""Which tool do you want to use?: 
        1. Add Items
        2. Remove Items
        3. Search For Items
        4. Reminder of what type this library is
        5. Exit \n"""))

        #Seeing if user input is 1 and then doing the add function for them
        if UserInput == 1:
            UserItemAdd = str(input("What do you want to add: "))
            AddItems(LibraryList, UserItemAdd)

        #Seeing if user input is 2 and then doing the remove function for them
        elif UserInput == 2:
            UserItemRemove = str(input("What do you want to remove?: "))
            RemoveItems(LibraryList, UserItemRemove)

        #Seeing if user input is 3 and then doing the search function for them
        elif UserInput == 3:
            UserItemSearch = int(input("Please give me the items order in the list by number (Such as 0, 1, 2, 3, etc...): "))
            SearchItems(LibraryList, UserItemSearch)

        #Seeing if user input is 4 and then reminding the user of the type of library this is
        elif UserInput == 4:
            print(f"The type of library you put this as is {UserTypeOfLibrary}.")
        
        #Seeing if user input is 5 and then exiting the library for the user
        elif UserInput == 5:
            print("Hope this library was useful goodbye!")
            break

main()