#Max Holdaway Word Counter Assignment: Word Counting function(s)
import csv

#Function to get the amount of words from the file
def reading_amount_of_words(file_name):
    index = 0
    words = 0
    with open(file_name, "r") as file:
        file_csv_reader = csv.reader(file, delimiter=" ")
        for row in file_csv_reader:
            for word in row:
                print(word)
                words = words + 1
                index = index + 1        
    print(words)
    return words