from django import forms

class SearchForm(forms.Form):
	search = forms.CharField(required=True, max_length=100, help_text='Search')