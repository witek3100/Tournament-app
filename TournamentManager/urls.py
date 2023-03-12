
from django.contrib import admin
from django.urls import include, path
from users import views

urlpatterns = [
    path('', include('main.urls')),
    path('usr/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('', include("django.contrib.auth.urls"))
]