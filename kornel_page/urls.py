from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.CoverPageView.as_view(), name="cover_page"),
]
