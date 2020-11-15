from helper_functions import *

# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    assert checkIfInputIsValid(year1, month1, day1), "year1, month1 or day1 are with incorrect values. Please check again"
    assert checkIfInputIsValid(year2, month2, day2), "year2, month2 or day2 are with incorrect values. Please check again"
    assert not dateIsBefore(year2, month2, day2, year1,month1,day1), 'first set is after second set. Fix that please'
    days = 0
    # YOUR CODE HERE!
    while dateIsBefore(year1,month1,day1,year2,month2,day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days