from django import forms
from django.forms import ModelForm
from landing.models import News

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ('title', 'description')