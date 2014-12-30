from entries.models import *

__author__ = 'rbonick'


def get_all_entries(user, date=None):
    """
    Gets all entries (tasks, events, notes) for a given date and user. If date is omitted, it will retrieve all entries.

    :param user: The user whose entries should be retrieved
    :param date: The date to retrieve entries from
    :return: A list of all entries for the user
    """

    if date:
        tasks = list(Task.objects.filter(author=user, date=date))
        notes = list(Note.objects.filter(author=user, date=date))
        events = list(Event.objects.filter(author=user, date=date))
    else:
        tasks = list(Task.objects.filter(author=user))
        notes = list(Note.objects.filter(author=user))
        events = list(Event.objects.filter(author=user))

    entries = tasks + notes + events
    return sorted(entries, key=lambda entry: entry.date_created)