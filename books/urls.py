from django.urls import path

from .views import BookListView, BookDetailView, BookDeleteView, BookUpdateView, SearchResultView
from . import views

urlpatterns = [
    path('', BookListView.as_view(), name="book_list"),
    path('create/', views.new_book_form_view, name="book_new"),
    path('<uuid:pk>/', BookDetailView.as_view(), name="book_detail"),
    path('<uuid:pk>/delete/', BookDeleteView.as_view(), name="book_delete"),
    path('<uuid:pk>/edit/', BookUpdateView.as_view(), name="book_edit"),
    path('<uuid:pk>/review/', views.review_book_form_view, name="book_review"),
    path('search-result/', SearchResultView.as_view(), name="search_result"),
]
