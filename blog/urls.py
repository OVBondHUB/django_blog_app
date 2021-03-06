from django.urls import path

from .views import *

urlpatterns = [
    path('', PostList.as_view(), name='post_list_url'),
    path('post/<str:slug>', PostDetail.as_view(), name='post_detail_url'),
    path('tags/', TagList.as_view(), name='tag_list_url'),
    path('tag/<str:slug>', TagDetail.as_view(), name='tag_detail_url')
]