from django import forms
from .models import Page, Contact

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
            'reference_two',
            'phone_one',
            'phone_two'
         ]

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields=[
            'name','rut', 'email', 'city', 'phone', 'gender', 'prevision', 'message'
        ]