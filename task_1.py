from datetime import datetime as dtdt

def get_days_from_today(date: str) -> int:
    ''' 
    Calculates the number of days between a given date and the current date.

    Param date - a string representing a date in the format 'YYYY-MM-DD'

    Returns:
    the number of days as integer | a negative value if:
        1) the given date is in the future;
        2) the date format is invalid.
    '''
    try:
        # Convert the input string into a datetime object
        custom_date = dtdt.strptime(date, '%Y-%m-%d')
        # Get current date as a datetime object
        current_date = dtdt.today()

        if custom_date > current_date:
            # handle the future date
            return -1
        else:
            # Calculate the difference in days
            result = (current_date - custom_date).days
            return result
    except ValueError:
        # handle invalid date format
        print("Invalid date format. Please use the format 'YYYY-MM-DD'.")
        return -1

print(get_days_from_today('2020-10-09'))