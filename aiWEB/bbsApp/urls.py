from django.urls import path
from bbsApp import views

urlpatterns = [
    # http://127.0.0.1:8000/bbs/index
    path('index/', views.index)
]