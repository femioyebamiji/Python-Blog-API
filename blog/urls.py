from django.urls import path
from blog.apiviews import ( ArticleListView, ArticleDetailView,
                            CategoryListView, CategoryDetailView,
                            JournalistListView, JournalistDetailView,
                            CommentDetailView, CommentListView )

urlpatterns = [
    path("articles/", ArticleListView.as_view(), name="article_list"),
    path("articles/<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category_detail"),
    path("journalists/", JournalistListView.as_view(), name="journalist_list"),
    path("journalists/<int:pk>/", JournalistDetailView.as_view(), name="journalist_detail"),
    path("comments/", CommentListView.as_view(), name="comment_list"),
    path("comments/<int:pk>/", CommentDetailView.as_view(), name="comment_detail"),
]