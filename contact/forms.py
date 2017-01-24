from django import forms

class Contactform(forms.Form):
	name = forms.CharField(required=True, max_length=100, help_text='100 letters max')
	email = forms.EmailField(required=False)
	comment = forms.CharField(required=True, widget= forms.Textarea)