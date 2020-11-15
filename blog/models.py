from django.db import models

# Create your models here.
class Journalist(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    short_profile = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Category(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    author = models.ForeignKey(Journalist, on_delete = models.CASCADE, related_name = "articles")
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = "articles")
    publication_date = models.DateTimeField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=256)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add =True)

    def __str__(self):
        return f"{self.name} {self.body}"
    