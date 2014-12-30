from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
# Handles registration
from user_mgmt.forms import UserRegistrationForm


def register(request):
    # Handles post of the form
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()

            # Log new user in
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)

            # Redirect to the home page
            return redirect('home')
        else:
            return render(request, 'login.html', {
                "registration_form": form,
            })
    # Otherwise just display the form
    else:
        form = UserRegistrationForm()
    return HttpResponseRedirect(reverse('django.contrib.auth.views.login'))