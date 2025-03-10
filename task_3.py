import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number: str) -> str:
    '''
    Normalizes a phone number by removing all characters except digits and '+'.
    If the number does not have an international code, it adds '+38' (for Ukraine).
    
    Params:
    phone_number: The phone number in any format as string.
    
    Returns:
    The normalized phone number in the correct format as string.
    '''
    # Format the string
    
    # Remove all characters except numbers and the '+' sign
    phone_number = re.sub(r"[^\d+]", "", phone_number)
    
     # Check if it is an international code (starts with '+')
    if re.match(r"^\+", phone_number):
        return phone_number
    
    # Check if the number starts with '380' and is without '+'
    if re.match(r"^380", phone_number):
        return "+" + phone_number
    
    # Add Ukrainian code '+38', if no international code is present
    return "+38" + phone_number

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)