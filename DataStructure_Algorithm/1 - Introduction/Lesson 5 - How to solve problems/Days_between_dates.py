from nextDay import nextDay

# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    days = 0
    # YOUR CODE HERE!
    while (year1 != year2) or (month1 != month2) or (day1 != day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

