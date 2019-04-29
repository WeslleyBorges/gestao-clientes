from django.urls import path, include

from home.views import MyView
from .views import home
from .views import my_logout
from django.views.generic.base import TemplateView
from .views import HomePageView

urlpatterns = [
    path('', home, name='home'),
    path('logout/', my_logout, name='my_logout'),
    path('home2/', TemplateView.as_view(template_name='home2.html'), name='logout'),
    path('home_dois/', HomePageView.as_view()),
    path('view/', MyView.as_view())
]




