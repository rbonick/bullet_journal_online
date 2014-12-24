__author__ = 'rbonick'

from datetime import date


def current_date_processor(request):
    current_date = date.today()
    return {'current_date': current_date}