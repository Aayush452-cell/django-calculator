from django.urls import path
from . import views
import calculator

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', calculator.views.index, name='index'),
    path('calci/', calculator.views.calci, name='calci'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/<int:user_id>', views.user_profile, name='profile'),
]