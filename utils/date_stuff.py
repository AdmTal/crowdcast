from datetime import datetime


def get_todays_date():
    # Get the current date
    current_date = datetime.now()

    # Define suffixes for day of the month
    suffixes = {1: 'st', 2: 'nd', 3: 'rd'}

    # I'm checking for 10-20 because those are the digits that
    # don't follow the normal st, nd, rd, th rule.
    if 10 <= current_date.day <= 20:
        suffix = 'th'
    else:
        # the last digit is all we need to find out the correct suffix
        suffix = suffixes.get(current_date.day % 10, 'th')

    return current_date.strftime(f"%A, %B {current_date.day}{suffix}, %Y")
