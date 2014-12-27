from datetime import date
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from dateutil.utils import get_dates, get_next_seven_days
from entries.forms import EntryCreationForm

from entries.utils import get_all_entries


def view_month_entries(request, month=date.today().month, year=date.today().year):
    user = get_object_or_404(User, username="rbonick")

    entries = {}
    month = int(month)
    year = int(year)
    for day in get_dates(month, year):
        entries[day] = get_all_entries(user, day)
    return render(request, 'entries.html', {
        "entries": sorted(entries.items()),
        "current_date": date.today(),
    })


def view_next_seven_days_entries(request):
    user = get_object_or_404(User, username="rbonick")

    entries = {}
    for day in get_next_seven_days():
        entries[day] = get_all_entries(user, day)
    print(sorted(entries.items()))
    return render(request, 'entries.html', {
        "entries": sorted(entries.items()),
    })


def create_entry(request):
    if request.method == 'POST':
        form = EntryCreationForm(request.POST)
        if form.is_valid():
            form.save(request.user)

            # Return user to the page they were on
            print("Next:", request.POST['next'])
            return HttpResponseRedirect(request.POST['next'])
        else:
            # This is a cheap hack, figure out a better solution
            return render(request, 'entries.html', {
                "form": form,
                "next": request.POST['next'],
            })