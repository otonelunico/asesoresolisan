from django import forms
from .models import Page

class PageForm(forms.ModelForm):

	class Meta:
		model=Page
		fields=[
			'title',
			'us_jpg1',
			'us_jpg2',
			'us',
			'note',
			'service_one',
			'service_two'
         ]