from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def index(request):
    return render(request, 'myapp/index.html')


def aries(request):
    post = Post.objects.order_by('-id')
    return render(request, 'myapp/aries.html', {'title': 'main', 'text': post})


def taurus(request):
    post = Post.objects.order_by('-id')
    return render(request, 'myapp/taurus.html', {'title': 'main', 'text': post})


def gemini(request):
    post = Post.objects.order_by('-id')
    return render(request, 'myapp/gemini.html', {'title': 'main', 'text': post})


def cancer(request):
    post = Post.objects.order_by('-id')
    return render(request, 'myapp/cancer.html', {'title': 'main', 'text': post})


def leo(request):
    post = Post.objects.order_by('-id')
    return render(request, 'myapp/leo.html', {'title': 'main', 'text': post})


def virgo(request):
    post = Post.objects.order_by('-id')
    return render(request, 'myapp/virgo.html', {'title': 'main', 'text': post})


def libra(request):
    post = Post.objects.order_by('-id')
    return render(request, 'myapp/libra.html', {'title': 'main', 'text': post})


def scorpio(request):
    post = Post.objects.order_by('-id')
    return render(request, 'myapp/scorpio.html', {'title': 'main', 'text': post})


def sagittarius(request):
    post = Post.objects.order_by('-id')
    return render(request, 'myapp/sagittarius.html', {'title': 'main', 'text': post})


def capricorn(request):
    post = Post.objects.order_by('-id')
    return render(request, 'myapp/capricorn.html', {'title': 'main', 'text': post})


def aquarius(request):
    post = Post.objects.order_by('-id')
    return render(request, 'myapp/aquarius.html', {'title': 'main', 'text': post})


def pisces(request):
    post = Post.objects.order_by('-id')
    return render(request, 'myapp/pisces.html', {'title': 'main', 'text': post})


def add(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form has error'

    form = PostForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'add.html', context)




