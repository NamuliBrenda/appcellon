from django.urls import path
from django.contrib.auth import views as auth_views
#from accounts.views import login_view, logout_view, home_view
from .views import register, login_view, logout_view, home_view, change_password
#from . import views


urlpatterns = [
    path('login/', login_view, name='login'),
    #path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='home'),
    path('signup/', register, name='register'),
    path('change_password/', change_password, name='change_password'),
]
