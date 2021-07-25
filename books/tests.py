from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Book, Review


class BookTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='Zasha',
            email='zashafachii@yahoo.com',
            password='testpass123',
        )

        self.book = Book.objects.create(
            title='Python the world',
            author="Zasha Fachiis",
            price='24.00',
        )

        self.review = Review.objects.create(
            book=self.book,
            author=self.user,
            review='An excellent book for learning python',
        )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Python the world')
        self.assertEqual(f'{self.book.author}', 'Zasha Fachiis')
        self.assertEqual(f'{self.book.price}', '24.00')

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Python')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/5687128')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'books/book_detail.html')
        self.assertContains(response, 'An excellent book for learning python')
