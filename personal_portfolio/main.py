#Max Holdaway Personal Portfolio

#Big huge import for all of my previous code (and inquirer)
from coin_main import main as coin_main
from movie_main import main as movie_main
from finance_main import main as finance_main
from to_do_main import main as to_do_main
from library_main import main as library_main
from multi_table import multi_table
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

#A function that is a confirmation that the user has read the decription or information
def confirmation():
    confirmation = inquirer.select(message='Choose Done Reading to continue', choices=['Done Reading']).execute()
    return confirmation

#A function that is template for a user input that lets the user select multiple options
def list_selection(message, choices):
    choice = inquirer.select(message=message, choices=choices).execute()
    return choice

#The user interface
def main():
    #Portfolio description
    print("This is my personal portfolio! It is a combination of the projects I think I have done my best on (including some old ones that were cool when I made them).")
    print("The way to use my portfolio is:\nYou can select one of my six projects to view and you can see an overview of what it does.\nIf you decide you want to use it you can do that as well simply select the run option.")
    #A "you have read" confirmation
    while True:
        confirm = confirmation()
        if confirm == 'Done Reading':
            break
    while True:
        #Using the template to see what the user wants to do in the portfolio
        user_input = list_selection('Which project do you want to see / use? Or do you want to exit:', ['Coin Change Program', 'Movie Recommender Program', 'Financial Calculator Program', 'To Do List Program', 'Personal Library Program', 'Multiplication Table Generator Program', 'Exit'])
        if user_input == 'Coin Change Program':
            #Until "user_choice" appears this is my project description
            while True:
                print('The Coin Change Program lets you give it an amount of money (with six different currencys to choose from) and show you all the coins inside that amount of money.')
                confirm = confirmation()
                if confirm == 'Done Reading':
                    break
            while True:
                print('I was able to find this programming process by figuring out how to split a number into a bunch of little parts.')
                confirm = confirmation()
                if confirm == 'Done Reading':
                    break
            while True:
                print('I learned from this that I way overcomplicated this project and that I need to get better at reducing my code size.')
                confirm = confirmation()
                if confirm == 'Done Reading':
                    break
            #Using the template to see if the user wants to actually run the program
            user_choice = list_selection('What do you want to do?', ['Run', 'Exit'])
            if user_choice == 'Run':
                #Using my imported code
                coin_main()
            elif user_choice == 'Exit':
                print('I hope this project was interesting!')
        elif user_input == 'Movie Recommender Program':
            #Until "user_choice" appears this is my project description
            while True:
                print('The Movie Recommender Program takes in filters and shows you a list of all the movies that fit said filter.')
                confirm = confirmation()
                if confirm == 'Done Reading':
                    break
            while True:
                print('I found the programming process through my ability to learn and a bit of help from my parents.')
                confirm = confirmation()
                if confirm == 'Done Reading':
                    break
            while True:
                print('I learned that the method of finding specific items in such a big list using code was not as difficult as expected.')
                confirm = confirmation()
                if confirm == 'Done Reading':
                    break
            #Using the template to see if the user wants to actually run the program
            user_choice = list_selection('What do you want to do?', ['Run', 'Exit'])
            if user_choice == 'Run':
                #Using my imported code
                movie_main()
            elif user_choice == 'Exit':
                print('I hope this project was interesting!')
        elif user_input == 'Financial Calculator Program':
            #Until "user_choice" appears this is my project description
            while True:
                print('The financial calculator program is a mini financial calculator that will help with finances.')
                confirm = confirmation()
                if confirm == 'Done Reading':
                    break
            while True:
                print('The process for this was mostly just figuring out how to do all the related math aspects for this program.')
                confirm = confirmation()
                if confirm == 'Done Reading':
                    break
            while True:
                print('I learned how to do math in coding much better from this project.')
                confirm = confirmation()
                if confirm == 'Done Reading':
                    break
            #Using the template to see if the user wants to actually run the program
            user_choice = list_selection('What do you want to do?', ['Run', 'Exit'])
            if user_choice == 'Run':
                #Using my imported code
                finance_main()
            elif user_choice == 'Exit':
                print('I hope this project was interesting!')
        elif user_input == 'To Do List Program':
            #Until "user_choice" appears this is my project description
            while True:
                print('This To Do List Program allows you to add, remove, and mark to do list items as done on a to do list.')
                confirm = confirmation()
                if confirm == 'Done Reading':
                    break
            while True:
                print('The process for the to do list was learning more about how to write and save information to files.')
                confirm = confirmation()
                if confirm == 'Done Reading':
                    break
            while True:
                print('I learned how to better manage information on files.')
                confirm = confirmation()
                if confirm == 'Done Reading':
                    break
            #Using the template to see if the user wants to actually run the program
            user_choice = list_selection('What do you want to do?', ['Run', 'Exit'])
            if user_choice == 'Run':
                #Using my imported code
                to_do_main([])
            elif user_choice == 'Exit':
                print('I hope this project was interesting!')
        elif user_input == 'Personal Library Program':
            #Until "user_choice" appears this is my project description
            while True:
                print('The Personal Library Program gives you a customizable library of songs that you can edit personally.')
                confirm = confirmation()
                if confirm == 'Done Reading':
                    break
            while True:
                print('The process of making this was a little bit difficult as I had to better learn how to find specific items in dictionaries.')
                confirm = confirmation()
                if confirm == 'Done Reading':
                    break
            while True:
                print('I learned how to better manage dictionaries and also how to better mange dictionaries related to files.')
                confirm = confirmation()
                if confirm == 'Done Reading':
                    break
            if user_choice == 'Run':
                #Using my imported code
                library_main()
            elif user_choice == 'Exit':
                print('I hope this project was interesting!')
        elif user_input == 'Multiplication Table Generator Program':
            #Until "user_choice" appears this is my project description
            while True:
                print('The Multiplication Table Generator Program is pretty self explanatory you give it a number and it gives you a table with all multiples of said number up to 12.')
                confirm = confirmation()
                if confirm == 'Done Reading':
                    break
            while True:
                print('The process for making this was figuring out how to increment the table while also saving all previous increments.')
                confirm = confirmation()
                if confirm == 'Done Reading':
                    break
            while True:
                print('I learned how to better increment and also save information.')
                confirm = confirmation()
                if confirm == 'Done Reading':
                    break
            #Using the template to see if the user wants to actually run the program
            user_choice = list_selection('What do you want to do?', ['Run', 'Exit'])
            if user_choice == 'Run':
                #Using my imported code
                multi_table()
            elif user_choice == 'Exit':
                print('I hope this project was interesting!')
        elif user_input == 'Exit':
            print('I hope you found my projects interesting goodbye!')
            break

main()