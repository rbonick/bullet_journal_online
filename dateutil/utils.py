__author__ = 'rbonick'

from datetime import date
from calendar import isleap

DAYS_PER_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def get_dates(month, year):
    """
    Returns a list of date objects for all days in the month and year provided.

    :param month: The month to retrieve dates for. Should be 1-based (month = 1 -> January).
    :param year: The year to retrieve dates for
    :return: A list of datetime.date objects for all days in the month and year provided
    """
    if month > 12 or month < 1 or year < 1900 or year > 9999:
        raise ValueError
    dates = []
    for day in range(1, DAYS_PER_MONTH[month - 1] + 1):
        dates.append(date(year, month, day))
    if month is 2 and isleap(year):
        dates.append(date(year, month, 29))
    return dates