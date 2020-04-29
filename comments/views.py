from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article
from .forms import CommentForm


def post_comment(request, article_id):
    post = get_object_or_404(Article, id=article_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = post
            comment.save()
            return redirect('blog:article', id=article_id)
    return redirect('blog:article', id=article_id)
