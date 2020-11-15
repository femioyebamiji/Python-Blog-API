from django.contrib import admin
from blog.models import Article, Category, Journalist, Comment

admin.site.register(Category)
admin.site.register(Journalist)
admin.site.register(Article)
admin.site.register(Comment)