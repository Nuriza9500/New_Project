from django.shortcuts import render
from main.models import News

def home(request):
    news = News.objects.all()
    context = {
        "news": news
    }
    return render(request, "index.html", context)