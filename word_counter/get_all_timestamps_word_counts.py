#Max Holdaway Word Counter Assignment: Showing all the word count and timestamp information function(s)
import csv

#Function to list all the file names with their corresponding info
def get_word_count_timestamp_info():
    with open("word_counter/saved_file_timestamps_word_counts.txt", "r") as file:
        csv_file_reader = csv.reader(file, delimiter = ",")
        for row in csv_file_reader:
            print(f"This is the file name: {row[2]}, This is the word count: {row[0]}, This is the timestamp: {row[1]}.")