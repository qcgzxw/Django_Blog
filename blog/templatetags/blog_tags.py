from django import template
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.aggregates import Count
from blog.models import Article, Category, Tag, Links, Carousel
from comments.models import Comments

register = template.Library()


@register.simple_tag
def get_carousel_list():
    """获取轮播图列表"""
    return Carousel.objects.all()


@register.simple_tag
def get_article_list(sort=None, num=None):
    """获取指定数量指定排序依据的文章"""
    if sort:
        if num:
            return Article.objects.filter(show=True).order_by(sort)[:num]
        return Article.objects.filter(show=True).order_by(sort)
    if num:
        return Article.objects.filter(show=True)[:num]
    return Article.objects.filter(show=True)


@register.simple_tag
def get_tag_list():
    """获取所有标签"""
    return Tag.objects.all()


@register.simple_tag
def get_category_list():
    """获取所有分类"""
    return Category.objects.all()


@register.simple_tag
def get_link_list():
    """获取所有链接"""
    return Links.objects.filter(show='True')


@register.simple_tag(takes_context=True)
def paginate(context,object_list,pages_count):
    """分页函数"""
    paginator = Paginator(object_list, pages_count)
    page = context['request'].GET.get('page')

    try:
        object_list = paginator.page(page)
        context['current_page'] = int(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
        context['current_page'] = 1
    except EmptyPage:
        object_list = paginator.page(Paginator.num_pages)
        context['current_page'] = Paginator.num_pages

    context['article_list'] = object_list
    context['pages'] = paginator.num_pages

    return ''
