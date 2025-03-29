from django.contrib import admin
from django.urls import path, include
from stories.views import MainPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage, name='MainPage'),
    path('stories/', include('stories.urls')),
    path('users/', include('users.urls')),
]