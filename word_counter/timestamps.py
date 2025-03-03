#Max Holdaway Word Counter Assignment: Timestamp function(s)

#Function to get the timestamp from the user
def get_timestamp():
    user_timestamp = ""
    print("Here you will enter the timestamp (when you found the wordcount)")
    user_year = input("What year is it? (type like 2020, 2022, 2024, 2025, etc...): ")
    user_month = input("What month is it? (type like 1, 2, 3, 4, etc...): ")
    user_day = input("What day is it? (type like 1, 10, 23, 15, etc...): ")
    user_hour = input("What hour is it? (type like 1, 2, 3, 4, etc...): ")
    user_pm_or_am = input("Is it Am or Pm?: ")
    user_minute = input("What is the current minute? (type like 10, 20, 30, 40, etc...): ")
    user_timestamp = user_timestamp + user_month + "/" + user_day + "/" + user_year + " " + "|||" + " " + user_hour + ":" + user_minute + " " + user_pm_or_am
    print(user_timestamp)
    return user_timestamp

get_timestamp()