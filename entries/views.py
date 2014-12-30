from collections import defaultdict
from datetime import date
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from dateutil.utils import get_dates, get_next_seven_days, get_months_until_today
from entries.forms import EntryCreationForm
from entries.models import Task

from entries.utils import get_all_entries


@login_required
def view_all_entries(request, future_only=False):
    entries = get_all_entries(request.user)

    entry_dict = defaultdict(list)

    for entry in entries:
        if future_only and (entry.date < date.today()):
            continue
        entry_dict[entry.date].append(entry)

    entries = sorted(entry_dict.items())
    request.session['entries'] = entries
    return render(request, 'entries.html', {
        "entries": entries,
    })



@login_required
def view_month_entries(request, month=date.today().month, year=date.today().year):
    user = request.user

    entries = {}
    month = int(month)
    year = int(year)
    for day in get_dates(month, year):
        entries[day] = get_all_entries(user, day)
    entries = sorted(entries.items())
    request.session['entries'] = entries
    return render(request, 'entries.html', {
        "entries": entries,
    })


@login_required
def view_next_seven_days_entries(request):
    user = request.user

    entries = {}
    for day in get_next_seven_days():
        entries[day] = get_all_entries(user, day)
    entries = sorted(entries.items())
    request.session['entries'] = entries
    return render(request, 'entries.html', {
        "entries": entries,
    })


@login_required
def create_entry(request):
    if request.method == 'POST':
        form = EntryCreationForm(request.POST)
        if form.is_valid():
            form.save(request.user)

            messages.success(request, "Entry successfully added.")

            # Return user to the page they were on
            return HttpResponseRedirect(request.POST['next'])
        else:
            # Keeps user on the same page if the form broke
            return render(request, 'entries.html', {
                "form": form,
                "next": request.POST['next'],
                "entries": request.session.get('entries'),
            })
    else:
        # If somehow gets a GET request, just redirect to the homepage
        return HttpResponseRedirect(reverse("home"))


def toggle_todo(request, todo_id):
    task = get_object_or_404(klass=Task, pk=todo_id)

    task.completed = not task.completed
    task.save()

    return HttpResponse("Successfully updated {0}".format(task.description))


def view_archive(request):
    months_years = get_months_until_today(request.user.date_joined.month, request.user.date_joined.year)

    months = []
    for month_year in months_years:
        month = date(month_year[1], month_year[0], 1)
        months.append(month)

    return render(request, 'archive.html', {
        "months": months,
    })