from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from blog.models import Article, Category, Journalist, Comment
from blog.serializers import (ArticleSerializer,
                              JournalistSerializer,
                              CategorySerializer,
                              CommentSerializer,
                              CommentSerializer)




class ArticleListView(APIView):

    def get(self, request):
        articles = Article.objects.filter(active=True)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status = status.HTTP_201_CREATED)
                        
        return Response(serializer.errors,
                        status = status.HTTP_400_BAD_REQUEST)

class ArticleDetailView(APIView):
    def get_object(self, pk):
        article = get_object_or_404(Article, pk=pk)
        return article

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer= ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)


class CategoryListView(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status = status.HTTP_201_CREATED)
                        
        return Response(serializer.errors,
                        status = status.HTTP_400_BAD_REQUEST)

class CategoryDetailView(APIView):
    def get_object(self, pk):
        category = get_object_or_404(Category, pk=pk)
        return category

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer= CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)





class JournalistListView(APIView):

    def get(self, request):
        journalists = Journalist.objects.all()
        serializer = JournalistSerializer(journalists, many=True, context = {'request':request})
        return Response(serializer.data)

    def post(self, request):
        serializer = JournalistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status = status.HTTP_201_CREATED)
                        
        return Response(serializer.errors,
                        status = status.HTTP_400_BAD_REQUEST)

class JournalistDetailView(APIView):
    def get_object(self, pk):
        journalist = get_object_or_404(Journalist, pk=pk)
        return journalist

    def get(self, request, pk):
        journalist = self.get_object(pk)
        serializer= JournalistSerializer(journalist, context = {'request':request})
        return Response(serializer.data)

    def put(self, request, pk):
        journalist = self.get_object(pk)
        serializer = JournalistSerializer(journalist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        journalist = self.get_object(pk)
        journalist.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)



class CommentListView(APIView):

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status = status.HTTP_201_CREATED)
                        
        return Response(serializer.errors,
                        status = status.HTTP_400_BAD_REQUEST)

class CommentDetailView(APIView):
    def get_object(self, pk):
        comment = get_object_or_404(Comment, pk=pk)
        return comment

    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer= CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)