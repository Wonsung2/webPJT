from django.urls import path
from blogApp import views

urlpatterns = [
    # http://127.0.0.1:8000/blog/index
    path('index/', views.index)
]