from django import template
from comments.models import Comments

register = template.Library()


@register.simple_tag
def get_comment_list(num=6):
    """获取侧边栏评论（默认6个）"""
    return Comments.objects.all().order_by('-date_publish')[:num]


@register.simple_tag
def get_comment_count(entry):
    """获取文章评论数量"""
    lis = entry.comments.all()
    return lis.count()


@register.simple_tag
def get_all_comment(entry):
    """获取文章评论"""
    lis = entry.comments.all()
    return lis


@register.simple_tag
def get_child_comment(com):
    """获取一个父评论的子评论"""
    child = com.c_id.all()
    return child


@register.simple_tag
def get_parent_comment(entry):
    """获取父评论"""
    parent = entry.comments.filter(p_id=None)
    return parent
