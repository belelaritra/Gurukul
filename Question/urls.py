from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # API to post comment
    path('comment', comment, name='comment'),

    # path('admin/', admin.site.urls),
    path('', feed, name='feed'),
    path('<str:slug>/', question, name='question'),
]