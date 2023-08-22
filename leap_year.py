"""
    A program that will check if a given year is a leap year or not
"""

def is_leap_year(year: int) -> bool:
    """
    Args:
        year (int): The year to be checked.

    Returns:
        bool: True if the year is a leap year and otherwise False.
    """
    if (year % 4) == 0: 
        if (year % 100 == 0) or (year % 400 != 0):
            return False
        else:
            # If the year is not divisible by 100 or is divisible by 400, a leap year.
            return True
    else:
        # If the year is not divisible by 4, not a leap year.
        return False


year = int(input("Year: "))
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

