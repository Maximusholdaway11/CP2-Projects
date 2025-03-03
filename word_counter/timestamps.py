#Max Holdaway Word Counter Assignment: Timestamp function(s)
def timestamp_checker(user_timestamp):
    user_timestamp_checker = input(f"is this timestamp correct?: {user_timestamp} Y/N: ")
    user_timestamp_checker = user_timestamp_checker.lower()
    return user_timestamp_checker

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
    if timestamp_checker(user_timestamp) == "y":
        return user_timestamp
    else:
        print("Okay here you can try and input it again.")
        user_year = input("What year is it? (type like 2020, 2022, 2024, 2025, etc...): ")
        user_month = input("What month is it? (type like 1, 2, 3, 4, etc...): ")
        user_day = input("What day is it? (type like 1, 10, 23, 15, etc...): ")
        user_hour = input("What hour is it? (type like 1, 2, 3, 4, etc...): ")
        user_pm_or_am = input("Is it Am or Pm?: ")
        user_minute = input("What is the current minute? (type like 10, 20, 30, 40, etc...): ")
        user_timestamp = user_timestamp + user_month + "/" + user_day + "/" + user_year + " " + "|||" + " " + user_hour + ":" + user_minute + " " + user_pm_or_am
        return user_timestamp