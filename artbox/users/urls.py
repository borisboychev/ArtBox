from django.urls import path

from users.views import profile_page, edit_profile, MyPasswordChangeView

urlpatterns = [
    path('profile/<int:id>', profile_page, name='profile page'),
    path('edit/<int:id>', edit_profile, name='edit profile'),
    path('change-password/', MyPasswordChangeView.as_view(), name='change password'),
]