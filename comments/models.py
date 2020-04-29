from django.db import models


class Comments(models.Model):
    name = models.CharField(max_length=30, verbose_name='昵称')
    email = models.EmailField(max_length=50, verbose_name='邮箱地址')
    url = models.URLField(max_length=50, blank=True, null=True, verbose_name='网址')
    content = models.TextField(verbose_name='评论内容')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')

    article = models.ForeignKey('blog.article', related_name='comments', on_delete=models.CASCADE)
    p_id = models.ForeignKey('self', related_name='c_id', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'blog_comments'
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)
