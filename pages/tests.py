from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutPageView


class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template_name(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contain_correct_html(self):
        self.assertContains(self.response, 'Cova')

    def test_homepage_contains_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi, I am not in the homepage')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )


class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template_name(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contain_correct_html(self):
        self.assertContains(self.response, 'About Page')

    def test_aboutpage_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'I am not in the about page')

    def test_aboutpage_urls_resolves_AboutPageView(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )
