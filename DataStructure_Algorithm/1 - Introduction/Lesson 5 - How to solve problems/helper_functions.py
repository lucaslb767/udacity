
def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """

    if day < checkHowManydays(year,month):
        return year, month, day + 1
    elif month < 12:
        return year, month + 1, 1
    else:
        return year + 1, 1, 1

def checkHowManydays(year, month):
    """Returns intenger with correct days for each month"""
    days_31 = [1,3,5,7,8,10,12]
    days_30 = [4,6,9,11]

    if month in days_31:
        return 31
    elif month in days_30:
        return 30
    else:
        if isLeapYear(year):
            return 29
        else:
            return 28




def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Checks if first set of date (year1, month1, day1) is before the second set of date"""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def isLeapYear(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

print(nextDay(2000, 2, 28))