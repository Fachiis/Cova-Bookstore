from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class ReviewTPage(TemplateView):
    template_name = 'pages/thanks.html'


class CreateTPage(TemplateView):
    template_name = 'pages/thanks2.html'


class ChargePageView(TemplateView):
    template_name = 'pages/charge.html'
