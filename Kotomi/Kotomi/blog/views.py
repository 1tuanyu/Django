from django.shortcuts import render
from blog.models import Article

# Create your views here.

def Home(request):
    articles = Article.objects.all()
    return render(request, 'home.html', {'articles':articles})

def Post(request):
    return render(request, 'post.html')

def Post_success(request):
    if request.POST:
        articles = request.POST['new_title']
        return render(request, 'post_success.html',{'articles':articles} )
    else:
        return render(request, 'error.html')







"""
    , new_title, new_label, new_content
    titles = [article.title for article in Article.objects.all()]
    new_title = request.POST['new_title']
    if new_title in titles:
        return render(request, 'error.html', {'error_message':'This article is already exist!'})
    else:
        new_article = Article(title=new_title, pub_date=timezone.now(), label=new_label, content=new_content)
        new_article.save()


def Post_success(request):
    if request.POST['new_content']:
        post_success = request.POST['new_content']
        return render(request, 'error.html')
    else:
        return render(reuqest, 'error.html')
"""




