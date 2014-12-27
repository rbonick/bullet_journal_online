from datetime import date
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from dateutil.utils import get_dates, get_next_seven_days
from entries.forms import EntryCreationForm
from entries.models import Task

from entries.utils import get_all_entries


@login_required
def view_month_entries(request, month=date.today().month, year=date.today().year):
    user = get_object_or_404(User, )

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
    user = get_object_or_404(User, username="rbonick")

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
            # This is a cheap hack, figure out a better solution
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