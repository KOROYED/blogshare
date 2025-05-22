from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path("posts/", views.PostListView.as_view(), name="blog_posts"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="blog_detail"),
    #re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),                    #same as above
    
]