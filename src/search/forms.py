from django import forms

class SearchForm(forms.Form):
	search = forms.CharField(label='Search Here', max_length=500)


