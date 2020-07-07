from django.shortcuts import render


def post_list(request):
    # TODO: Add posts
    posts = ['Post A', 'Post B']
    return render(request, 'blog/index.html', context={'posts': posts})

