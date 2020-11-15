from rest_framework import serializers
from blog.models import Article, Category, Journalist, Comment
from datetime import datetime
from django.utils.timesince import timesince



class ArticleSerializer(serializers.ModelSerializer):

    

    class Meta:
        model = Article
        fields = "__all__"
    
    # def get_time_since_publication(self, object):
    #     publication_date = object.publication_date
    #     now = datetime.now()
    #     time_delta = timesince(publication_date, now)
    #     return time_delta

    def validate(self, data):
        """ Check if title and description are the same - object level validation"""
        if data["title"] == data["body"]:
            raise serializers.ValidationError("Title cannot be exactly the same as body")
        return data

    def validate_body(self, value):
        """ Field level validation"""
        if len(value) < 15:
            raise serializers.ValidationError("Body cannot be less than 15 characters")
        return value



class CategorySerializer(serializers.ModelSerializer):

    articles = ArticleSerializer(many = True, read_only=True)
    class Meta:
        model = Category
        fields = "__all__"

class JournalistSerializer(serializers.ModelSerializer):
    
    articles = ArticleSerializer(many = True, read_only=True)
    class Meta:
        model = Journalist
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"