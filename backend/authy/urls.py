from django.urls import path
from authy.views import (EditProfile, register, upload_passport, login_view,
                         logout_view, change_password)

urlpatterns = [
    # Profile Section
    path('passport/', upload_passport, name="passport"),
    path('edit-profile/', EditProfile, name="edit-profile"),

    # User Authentication
    path('sign-up/', register, name="sign-up"),
    path('sign-in/', login_view, name='sign-in'),
    path('sign-out/', logout_view, name='sign-out'),
    path('change-password/', change_password, name='change-password'),
]
