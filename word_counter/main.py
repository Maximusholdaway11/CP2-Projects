#Max Holdaway Word Counter Assignment: Main User Interface / The Main Function

import add_timestamp_and_word_count
import timestamps
import word_counting

def main():
    user_input = input("Which option do you want to do?\n1. Getting the word count and adding the timestamp of a file\n2. Exit\n")
    if user_input.isnumeric():
        user_input = int(user_input)
        if user_input == 1:
            user_file_name = input("What is the relative path of the file you want to use for this?: ")
            word_count = word_counting.reading_amount_of_words(user_file_name)
            timestamp = timestamps.get_timestamp()
            if add_timestamp_and_word_count.add_timestamp_and_word_count(word_count, timestamp, user_file_name):
                print("File successfully word counted and timestamped.")
                print("FYI There is a seperate file that holds this information IT IS NOT ON YOUR FILE. (the file name is )")
            else:
                print("An unexpected error has occured please restart the program.")