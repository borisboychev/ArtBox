from django.urls import path

from art.views import delete_art, create_art, edit_art, HomePageView, GalleryView

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home page'),
    path('gallery/', GalleryView.as_view(), name='gallery page'),
    path('delete/<int:id>', delete_art, name='delete art'),
    path('create/', create_art, name='create art'),
    path('edit/<int:id>', edit_art, name='edit art')
]