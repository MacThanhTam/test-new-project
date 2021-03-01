from django.urls import path
from .views import user_register,user_login,user_profile
from .import views

urlpatterns = [
    path('register/',views.user_register,name='register'),
    path('login/',views.user_login, name='login'),
    path('profile/',views.user_profile, name='profile'),

]
