
def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """

    if day < 30:
        return year, month, day + 1
    elif month < 12:
        return year, month + 1, 1
    else:
        return year + 1, 1, 1
