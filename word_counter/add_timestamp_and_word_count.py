#Max Holdaway Word Counter Assignment: Adding Word Count and Timestamp function(s)
import csv

#Function to save the word count and timestamp of a specific file
def add_timestamp_and_word_count(user_word_count, user_timestamp, file_name):
    with open("word_counter/txt_file_timestamps_and_word_counters.txt", "w") as file:
        file_csv_writer = csv.writer(file)
        file_info_dict = {"word_count": user_word_count, "timestamp": user_timestamp, "file_name": file_name}
        file_csv_writer.writerow(file_info_dict, delimiter = "")