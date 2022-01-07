from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # API to post comment
    # path('admin/', admin.site.urls),
    path("", feed, name="feed"),
    path("upload/", Upload, name="upload"),
]
