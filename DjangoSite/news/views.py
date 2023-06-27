from django.shortcuts import render, get_object_or_404

# Create your views here.
from news.models import Article


def index(request):
    return render(request, "index.html")


def blogHome(request):
    lastArticle = Article.objects.all().reverse()
    return render(request, "blogHome.html", context={"articles": lastArticle})

def articleDetail(request,slug):
    article=get_object_or_404(Article,slug=slug)
    return render(request,"articleDetail.html",context={"content":article.contenu})


