from django.urls import path

from art.views import home_page, gallery, delete_art, create_art

urlpatterns = [
    path('home/', home_page, name='home page'),
    path('gallery/', gallery, name='gallery page'),
    path('delete/<int:id>', delete_art, name='delete art'),
    path('create/', create_art, name='create art'),
]