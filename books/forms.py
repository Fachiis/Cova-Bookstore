from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper

from .models import Review, Book


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review']


class BookForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.include_media = False
        super(ModelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'cover']

        widgets = {
            'cover': forms.FileInput()
        }
