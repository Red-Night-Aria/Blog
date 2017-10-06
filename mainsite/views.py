from django.shortcuts import render
from .models import Post
from django.http import Http404
from math import ceil

# Create your views here.
def index(request):
    return page(request, 1)


ENTRY_PER_PAGE = 2
def page(request, num):
    num = int(num)
    posts = Post.objects.all()

    if (num-1)*ENTRY_PER_PAGE >= len(posts):
        raise Http404("Oops, 找不到指定页面")

    ctx = {
        'posts': posts.order_by('-pub_date')[(num-1)*ENTRY_PER_PAGE: min(num*ENTRY_PER_PAGE, len(posts))],
        'page': num,
        'maxPage': ceil(len(posts)/ENTRY_PER_PAGE)
    }

    for post in ctx['posts']:
        post.day = post.pub_date.strftime('%d')
        post.month = post.pub_date.strftime('%b')

    return render(request, 'index.html', ctx)


def post(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404("Oops, 找不到指定文章") 

    post.day = post.pub_date.strftime('%d')
    post.month = post.pub_date.strftime('%b')

    ctx = {
        'post': post
    }

    return render(request, 'post.html', ctx)

def chatter(request):
    return render(request, 'chatter.html')