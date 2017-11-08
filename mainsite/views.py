from django.shortcuts import render
from .models import Post, Pastime
from django.http import Http404, HttpResponseNotFound
from math import ceil

# Create your views here.
def index(request):
    return page(request, 1)


ENTRY_PER_PAGE = 5
def page(request, num):
    num = int(num)
    posts = Post.objects.all()

    if (num-1)*ENTRY_PER_PAGE >= len(posts):
        return HttpResponseNotFound("<h1>很遗憾，这个博主似乎有些懒散。</h1>")

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
        'post': post,
        'currentPath': request.get_full_path()
    }

    return render(request, 'post.html', ctx)

def chatter(request):
    return render(request, 'chatter.html', {'currentPath': request.get_full_path()})

def pastime(request):
    ctx = {
        'items' : Pastime.objects.all()
    }
    return render(request, 'pastime.html', ctx)

def FM(request):
    return render(request, 'FM.html', {'currentPath': request.get_full_path()})
