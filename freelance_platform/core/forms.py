from django import forms
from django.contrib.auth.models import User
from .models import Project, Bid

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'budget']

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount', 'message']