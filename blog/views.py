from django.views.generic import View

from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectListMixin


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostList(ObjectListMixin, View):
    model = Post
    template = 'blog/index.html'
    context_list_name = 'posts'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagList(ObjectListMixin, View):
    model = Tag
    template = 'blog/tags.html'
    context_list_name = 'tags'




