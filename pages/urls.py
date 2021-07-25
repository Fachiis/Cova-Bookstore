from django.urls import path

from .views import HomePageView, AboutPageView, ReviewTPage, CreateTPage, ChargePageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('charge/', ChargePageView.as_view(), name="charge"),
    path('thanks-review/', ReviewTPage.as_view(), name="thanks_review"),
    path('thanks-book/', CreateTPage.as_view(), name="thanks_book"),
]
