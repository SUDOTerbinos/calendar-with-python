import calendar

def display_calendar():
    print("Simple Calendar Program")
    print("=======================")

    year = int(input("Enter year (e.g., 2025): "))
    month = int(input("Enter month (1-12): "))

    try:
        print("\n", calendar.month(year, month))
    except IndexError:
        print("Invalid month entered! Please enter a value between 1 and 12.")

if __name__ == "__main__":
    display_calendar()
