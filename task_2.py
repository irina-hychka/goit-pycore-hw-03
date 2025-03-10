import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """
    Generates a sorted list of unique random numbers in range.
    
    Params:
    min - the minimum number(inclusive): is not less than 1.
    max: The maximum number(inclusive): does not exceed 1000.
    quantity: the number to choose (value between min and max).

    Returns:
    A sorted list of unique random numbers | An empty list if at least one of params fails.
    """
    numbers = []

    # Check all params are integers
    if not all(isinstance(i, int) for i in [min, max, quantity]):
        return numbers
    
    # Check min is grater than 0 and max does not exceed 1000
    if min < 1 or max > 1000:
        return numbers
    
    # Check min value is not grater than max value
    if min >= max:
        return numbers
    
    # Check quantity is in range
    if quantity < min or quantity > max:
        return numbers
    
    # generate a list of unique numbers in range
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)
    
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)