from django.contrib.auth import views as auth_views
from django.urls import path
from authy.views import EditProfile, register, upload_passport

urlpatterns = [
    # Profile Section
    path('edit-profile', EditProfile, name="editprofile"),
    path('passport', upload_passport, name="passport"),

    # User Authentication
    path('sign-up/', register, name="sign-up"),
    path('sign-in/', auth_views.LoginView.as_view(template_name="sign-in.html", redirect_authenticated_user=True), name='sign-in'),
    path('sign-out/', auth_views.LogoutView.as_view(template_name="sign-out.html"), name='sign-out'), 
]
