from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # Get current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format to "YYYY-MM-DD HH:MM:SS"
    print(f"Current date and time: {formatted_date}")

# Part 2: Calculate a Future Date
def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)  # Add days
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

# Main Program
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
