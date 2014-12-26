__author__ = 'rbonick'

from django import forms
from entries.models import *


TASK = "task"
NOTE = "note"
EVENT = "event"

ENTRY_CHOICES = (
    (None, ""),
    (TASK, 'Task'),
    (NOTE, 'Note'),
    (EVENT, 'Event'),
)


class EntryCreationForm(forms.Form):
    type = forms.ChoiceField(label="Type", choices=ENTRY_CHOICES, error_messages={'required': 'Please select the type of event'})
    entry = forms.CharField(label="Entry", error_messages={'required': 'Please enter some text for your entry'})
    date = forms.DateField(label="Date", error_messages={'required': 'Please choose a date for your entry'})

    priority = forms.BooleanField(label="Priority", required=False)
    explore = forms.BooleanField(label="Explore", required=False)
    inspiration = forms.BooleanField(label="Inspiration", required=False)

    def save(self, user):
        if self.is_valid():
            if self.cleaned_data['type'] == TASK:
                model = Task()
            elif self.cleaned_data['type'] == NOTE:
                model = Note()
                model.explore = self.cleaned_data['explore']
                model.inspiration = self.cleaned_data['inspiration']
            elif self.cleaned_data['type'] == EVENT:
                model = Event()

            print(type(model))

            model.date = self.cleaned_data['date']
            model.description = self.cleaned_data['entry']
            model.author = user

            model.save()