from django.contrib import admin
from django.urls import path
from .views import trial,hello,group
urlpatterns = [
    path('',trial),
	path('',hello),
    path('',group)
]
