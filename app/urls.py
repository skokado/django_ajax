  
from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/', views.ajax, name='ajax'),
    path('greet/', views.GreetView.as_view(), name='greet'),
    path('auto/', views.AutoDisplayView.as_view(), name='auto'),
]
