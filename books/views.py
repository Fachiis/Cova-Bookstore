""" This module provides the business logic for the article and review. """
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Book
from .forms import ReviewForm, BookForm


@login_required
def review_book_form_view(request, pk):
    """
    Create a review obj on a book instance by the logged in user

    Args:
        request (objs): ...body(logged in user)
        pk (int): selected book obj or instance

    Returns:
        render: render request obj, template use, context
    """
    book_instance = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            saving = form.save(commit=False)
            saving.author_id = request.user.id
            saving.book_id = book_instance.id
            saving.save()
            return HttpResponseRedirect(reverse_lazy("thanks_review"))
    else:
        form = ReviewForm()
    context = {"form": form}
    return render(request, "books/review_form.html", context)


@login_required
def new_book_form_view(request):
    """
    Create a new book obj by logged in user

    Args:
        request (objs): ..body(logged in user)

    Returns:
        render: render request obj, template use, context
    """
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            saving = form.save(commit=False)
            saving.uploader_id = request.user.id
            saving.save()
            return HttpResponseRedirect(reverse_lazy("thanks_book"))
    else:
        form = BookForm()
    context = {"form": form}
    return render(request, "books/book_create.html", context)


class BookListView(LoginRequiredMixin, ListView):
    """A Book View class for listing all available book objs."""

    model = Book
    context_object_name = "book_list"
    template_name = "books/book_list.html"


class BookDetailView(LoginRequiredMixin, DetailView):
    """A Book View class for listing a book obj."""

    model = Book
    context_object_name = "book"
    template_name = "books/book_detail.html"


class BookDeleteView(LoginRequiredMixin, DeleteView):
    """
    A Book View class for deleting a book obj.
    """

    model = Book
    context_object_name = "book"
    template_name = "books/delete_book.html"
    success_url = reverse_lazy("book_list")


class BookUpdateView(LoginRequiredMixin, UpdateView):
    """
    A Book View class for updating the title, author and price of a book obj.
    """

    model = Book
    fields = ["title", "author", "price"]
    context_object_name = "book"
    template_name = "books/edit_book.html"

    def get_success_url(self):
        return reverse("book_detail", kwargs={"pk": self.object.pk})


class SearchResultView(LoginRequiredMixin, ListView):
    """
    Create a search functionality for books

    Returns:
        query: all available or related book with the key search
    """

    model = Book
    context_object_name = "book_list"
    template_name = "books/search_results.html"

    def get_queryset(self):
        search_key = self.request.GET.get("q")
        query = Book.objects.filter(
            Q(title__icontains=search_key) | Q(author__icontains=search_key)
        )
        return query
