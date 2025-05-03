from django.shortcuts import render
from .models import Article
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import ArticleForm

def index(request):
    articles = Article.objects.order_by('-date')  # Самые новые новости первыми
    return render(request, 'index.html', {'articles': articles})


def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('index')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



def add_article_view(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ArticleForm()
    return render(request, 'add_article.html', {'form': form})
