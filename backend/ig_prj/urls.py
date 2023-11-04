from django.contrib import admin
from django.urls import path, include
from authy.views import UserProfile, follow

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('authy.urls')),
    path('', include('post.urls')),
    path('message/', include('directs.urls')),
    path('notifications/', include('notification.urls')),

    # profile
    path('<username>/', UserProfile, name='profile'),
    path('<username>/saved/', UserProfile, name='profilefavourite'),
    path('<username>/follow/<option>/', follow, name='follow'),
]
