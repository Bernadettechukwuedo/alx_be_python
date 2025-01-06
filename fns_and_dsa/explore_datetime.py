import datetime


def display_current_datetim():
    current_date = datetime.datetime.now()
    return current_date.strftime("%Y-%m-%d %H:%M:%S")


def calculate_future_date(number_of_days):
    future_date = datetime.datetime.now() + datetime.timedelta(days=number_of_days)
    return future_date.strftime("%Y-%m-%d")


print(f"Current date and time: {display_current_datetim()}")
prompt = int(input("Enter the number of days to add to the current date:"))
print(f"Future date: {calculate_future_date(prompt)}")
