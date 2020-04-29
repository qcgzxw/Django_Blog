from django.db import models


# 博客友链
class Links(models.Model):
    url = models.URLField(verbose_name='链接地址')
    name = models.CharField(max_length=50, verbose_name='站点名称')
    description = models.CharField(max_length=100, verbose_name='站点描述')
    show = models.BooleanField(default=False, verbose_name='是否显示')
    time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    index = models.IntegerField(default=99, verbose_name='排列顺序（从小到大）')

    class Meta:
        db_table = 'blog_links'
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
        ordering = ['index', '-id']

    def __str__(self):
        return self.name


# 博客轮播图
class Carousel(models.Model):
    url = models.URLField(verbose_name='链接地址')
    title = models.CharField(max_length=20, verbose_name='图片标题')
    description = models.CharField(max_length=40, verbose_name='图片描述')
    image = models.URLField(verbose_name='图片地址')
    index = models.IntegerField(default=999, verbose_name='轮播图顺序（从小到大）')

    class Meta:
        db_table = 'blog_carousel'
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
        ordering = ['index', '-id']

    def __str__(self):
        return self.title


# 博客配置
class Settings(models.Model):
    title = models.CharField(max_length=30, verbose_name='站点标题')
    subtitle = models.CharField(max_length=50, verbose_name='站点副标题')
    keywords = models.CharField(max_length=300, verbose_name='站点关键词（最大长度300）')
    description = models.CharField(max_length=150, verbose_name='站点描述（最大长度150）')
    favicon = models.URLField(verbose_name='站点小图标地址')
    logo = models.URLField(verbose_name='站点Logo地址')

    class Meta:
        db_table = 'blog_settings'
        verbose_name = '全局设置'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 博客分类
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='分类名称')
    slug = models.SlugField(max_length=30, unique=True, verbose_name='固定链接')
    description = models.CharField(max_length=200, verbose_name='分类描述')
    index = models.IntegerField(default=999, verbose_name='分类权重')

    class Meta:
        db_table = 'blog_category'
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.name


# 博客标签
class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='标签名称')
    index = models.IntegerField(default=999, verbose_name='标签权重')

    class Meta:
        db_table = 'blog_tags'
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.name


# 文章管理类
class ManagerArticle(models.Manager):
    def distinct_date(self):
        distinct_date_list = []
        date_list = self.values('date_publish')
        for date in date_list: 
            date = date['date_publish'].strftime('%Y/%m文章存档')
            if date not in distinct_date_list:
                distinct_date_list.append(date)
        return distinct_date_list


# 博客文章
class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='文章标题')
    author = models.CharField(max_length=30, verbose_name='文章作者')
    description = models.CharField(max_length=200, verbose_name='文章描述')
    content = models.TextField(verbose_name='文章内容')
    thumb = models.URLField(default='https://ww2.sinaimg.cn/large/a15b4afegy1fil8yrpuejj212w0p5n09.jpg', verbose_name='特色图')
    views = models.IntegerField(default=0, verbose_name='浏览量')
    is_recommand = models.BooleanField(default=False, verbose_name='是否推荐')
    show = models.BooleanField(default=True, verbose_name='是否显示')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布日期')
    love = models.IntegerField(default=0, verbose_name='点赞数')

    tag = models.ManyToManyField('Tag', verbose_name='文章标签', related_name='article')
    category = models.ManyToManyField('Category', verbose_name='文章分类', related_name='article')

    objects = ManagerArticle()

    class Meta:
        db_table = 'blog_article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __str__(self):
        return self.title

    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])

    def like(self):
        self.love += 1
        self.save(update_fields=['love'])

    def dislike(self):
        self.love -= 1
        self.save(update_fields=['love'])
