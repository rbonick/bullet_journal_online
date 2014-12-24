from datetime import date
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from dateutil.utils import get_dates

from entries.utils import get_all_entries


def view_month_entries(request, month=date.today().month, year=date.today().year):
    user = get_object_or_404(User, username="rbonick")

    entries = {}
    month = int(month)
    year = int(year)
    for date in get_dates(month, year):
        entries[date] = get_all_entries(user, date)
    return render(request, 'entries.html', {
        "entries": entries,
        "current_date": date.today(),
    })