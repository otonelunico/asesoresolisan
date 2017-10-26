from django import forms
from .models import Page

class PageForm(forms.ModelForm):

	class Meta:
		model=Page
		fields=[
			'title',
			'us_img1',
			'us_img2',
			'us',
			'note',
			'service_img',
			'service_one',
			'service_two',
            'reference_one',
            'reference_tree',
            'reference_two'
         ]