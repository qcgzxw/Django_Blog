from django.contrib import admin
from blog.models import Article, Category, Links, Tag, Settings, Carousel

# Register your models here.
admin.site.register(Links)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Settings)
admin.site.register(Carousel)
