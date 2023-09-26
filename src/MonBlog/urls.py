from os import path

from src.MonBlog.views import index
urlpatterns = [
    path('', index),
]