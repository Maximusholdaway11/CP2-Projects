#Max Holdaway Word Counter Assignment: Main User Interface / The Main Function

#Importing all the functions from the other pages
import add_timestamp_and_word_count
import timestamps
import word_counting
import get_all_timestamps_word_counts

#Main user interface
def main():
    while True:
        user_input = input("Which option do you want to do?\n1. Getting the word count and adding the timestamp of a file\n2. Show a list of all the information related to word count and timestamps for each file\n3. Exit\n")
        if user_input.isnumeric():
            user_input = int(user_input)
            if user_input == 1:
                try:
                    user_file_name = input("What is the relative path of the file you want to use for this?: ")
                    word_count = word_counting.reading_amount_of_words(user_file_name)
                    timestamp = timestamps.get_timestamp()
                    add_timestamp_and_word_count.add_timestamp_and_word_count(word_count, timestamp, user_file_name)
                    print("File successfully word counted and timestamped.")
                    print("FYI There is a seperate file that holds this information IT IS NOT ON YOUR FILE. (the file name is saved file timestamps word counts its a .txt file)")
                except FileNotFoundError as e:
                    print(f"FileNotFoundError occurred {e} (this file either does not exist or you didn't put it in correctly)")
                    continue
            elif user_input == 2:
                try:
                    get_all_timestamps_word_counts.get_word_count_timestamp_info()
                except:
                    print("Unexpected Error Has Occured.")
            elif user_input == 3:
                print("Hope this was useful goodbye!")
                break

main()