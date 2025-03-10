from datetime import datetime as dtdt, timedelta as td

def get_upcoming_birthdays(users):
    """
    Retrieves a list of upcoming birthdays in the next 7 days.
    If a birthday falls on a weekend (Saturday or Sunday), 
    the congratulation date is moved to Monday.
    
    Params:
    users: List of dictionaries, each containing "name" and "birthday"
    (format: "YYYY.MM.DD")

    Returns:
    List of dictionaries with "name" and adjusted "congratulation_date" 
    or empty list if there are no birthdays
    """
    current_date = dtdt.today().date()
    upcoming_birthdays = []
    
    for user in users:
        name = user["name"]
        birthday = dtdt.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # Replace year with current year
        birthday_this_year = birthday.replace(year=current_date.year)
        
        # Get next year if birthday has passed
        if birthday_this_year < current_date:
            birthday_this_year = birthday_this_year.replace(year=current_date.year + 1)
        
        # Check if the birhday is in range of next 7 days
        if 0 <= (birthday_this_year - current_date).days <= 7:
            congratulation_date = birthday_this_year
            
            # Move Birthday on Monday if it is on weekdays
            if congratulation_date.weekday() in [5, 6]:
                congratulation_date += td(days=(7 - congratulation_date.weekday()))
            
            upcoming_birthdays.append({
                "name": name,
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Sarah Smith", "birthday": "1978.3.10"},
    {"name": "Tom Smith", "birthday": "2000.3.15"},
]

print(get_upcoming_birthdays(users))