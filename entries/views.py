from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from entries.utils import get_all_entries


def view_all_entries(request):
    user = get_object_or_404(User, username="rbonick")

    return render(request, 'entries.html', {
        "entries": get_all_entries(user)
    })