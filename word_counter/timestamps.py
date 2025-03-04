#Max Holdaway Word Counter Assignment: Timestamp function(s)
import datetime
import pytz

#Function to get the timestamp for the file
def get_timestamp():
    tz = pytz.timezone('America/Denver')
    user_timestamp = datetime.datetime.strftime(datetime.datetime.now(tz=tz), '%d/%m/%y %H:%M:%S')
    return user_timestamp