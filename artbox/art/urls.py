from django.urls import path

from art.views import home_page

urlpatterns = [
    path('home/', home_page, name='home page'),
]