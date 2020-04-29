from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils.text import slugify
from django.db.models import Q
from blog.models import Category, Tag, Article

from markdown.extensions.toc import TocExtension  # 锚点的拓展
import markdown


# Create your views here.
def index(request):
    return render(request, 'index.html', locals())


def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    article.views += 1
    article.save()
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        TocExtension(slugify=slugify)
    ])
    article.body = md.convert(article.content)
    article.toc = md.toc
    return render(request, 'article.html', {'article': article})


def links(request):
    return render(request, 'link.html', locals())


def about(request):
    return render(request, 'about.html', locals())


def contact(request):
    return render(request, 'contact.html', locals())


def tag_detail(request, id):
    tag = get_object_or_404(Tag, id=id)
    return render(request, 'tag.html', {'article_list': tag.article.filter(show=True),
                                        'article_count': tag.article.filter(show=True).count,
                                        'tag_name': tag.name})


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'category.html', {'article_list': category.article.filter(show=True),
                                             'article_count': category.article.filter(show=True).count,
                                             'category_name': category.name,
                                             'category_description': category.description})


def search(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword')
        if keyword:
            article_list = Article.objects.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword)).filter(
                show=True)
            return render(request, 'search.html', {'article_list': article_list,
                                                   'article_count': article_list.count,
                                                   'keyword': keyword})
        else:
            return redirect('blog:index')
    else:
        return redirect('blog:index')


def error(request):
    if request.method == 'GET':
        errmsg = request.GET.get('errmsg')
        return HttpResponse("Error Message: %s." % errmsg)
