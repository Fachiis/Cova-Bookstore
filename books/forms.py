""" This module provides the function to create a book and review form object. """
from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper

from .models import Review, Book


class ReviewForm(ModelForm):
    """
    A Review Form class for creating a review object.
    """

    class Meta:
        """Meta class for ReviewForm control."""

        model = Review
        fields = ["review"]


class BookForm(ModelForm):
    """
    A Book Form class for creating a book object.
    """

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.include_media = False
        super(ModelForm, self).__init__(*args, **kwargs)

    class Meta:
        """Meta class for BookForm control."""

        model = Book
        fields = ["title", "author", "price", "cover"]

        widgets = {"cover": forms.FileInput()}
