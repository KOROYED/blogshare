from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("category/<category>/", views.PostByCategoryListView.as_view(), name="blog_category"),
    path("posts/", views.PostListView.as_view(), name="blog_posts"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("authors/", views.AuthorListView.as_view(), name="blog_authors"),
    path("author/<int:pk>/", views.AuthorDetailView.as_view(), name="blog_author_detail"),
    path("author/<int:pk>/posts", views.AuthorPostListView.as_view(), name="blog_author_posts"),
    path("author/<int:pk>/comments", views.AuthorCommentListView.as_view(), name="blog_author_comments"),
    path("signup/", views.SignUpView.as_view(), name="blog_signup")
    #re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),                    #same as above
    
]