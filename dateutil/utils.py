__author__ = 'rbonick'

from datetime import date, timedelta
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


def get_next_seven_days(day=date.today()):
    """
    Returns a list of date objects for the current day and the following six days.

    :param day: The current date
    :return: A list of datetime.date objects for today and the next six days
    """
    dates = []
    for day_increment in range(0, 7):
        dates.append(day + timedelta(days=day_increment))
    return dates


def get_months_until_today(start_month, start_year):
    """
    Returns a list of tuples for all months/years beginning at the given month and ending at the current month

    :param start_month: The month to begin at
    :param start_year: The year to begin at
    :return: A list of tuples in the format (month, year) from the given month/year to the current month/year
    """
    if start_month > 12 or start_month < 1 or start_year < 1900 or start_year > date.today().year:
        raise ValueError

    months = []
    for year in range(start_year, date.today().year + 1):
        for month in range(start_month, 13):
            # Break case
            if (year == date.today().year) and (month == date.today().month):
                months.append((month, year))
                return months
            months.append((month, year))
        start_month = 1