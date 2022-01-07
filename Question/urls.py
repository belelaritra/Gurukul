from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # API to post comment
    path("comment", comment, name="comment"),
    path("uploadquestion", uploadquestion, name="uploadquestion"),
    # path('admin/', admin.site.urls),
    path("", feed, name="feed"),
    path("<str:slug>/", question, name="question"),
    path("filter", filter, name="filter"),
    path("edit_question", edit_question, name="edit_question"),
    path("delete_question", delete_question, name="delete_question"),
    path("edit_answer", edit_answer, name="edit_answer"),
    path("delete_answer", delete_answer, name="delete_answer"),
    path("edit_reply", edit_reply, name="edit_reply"),
    path("delete_reply", delete_reply, name="delete_reply"),
]
