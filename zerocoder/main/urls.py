from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new, name='page2'),
    path('second', views.second, name='page3'),
    path('third', views.third, name='page4')
]
