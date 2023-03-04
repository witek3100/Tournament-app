
from django.contrib import admin
from django.urls import include, path
from users import views

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login")
]