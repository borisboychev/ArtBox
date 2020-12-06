from django.urls import path

from art.views import home_page, gallery

urlpatterns = [
    path('home/', home_page, name='home page'),
    path('gallery/', gallery, name='gallery page'),
]