from django.shortcuts import render
from .models import Post, Comment
from django.views import generic

def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")                                              # - in -created_on  reverses arrangment of objects by order_by
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context=context)

def blog_category(request, category):
    posts = Post.objects.filter(category__name__contains = category).order_by("-created_on")        # category__name coz many to many field
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context=context)

# def blog_detail(request, pk):
#     post = Post.objects.get(pk=pk)                                                                  # pk = primary key
#     comments = Comment.objects.filter(post=post)
#     context = {
#         "post": post,
#         "comments": comments,
#     }
    
#     return render(request, "blog/detail.html", context)


class PostListView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    queryset = Post.objects.filter(title__icontains='poe')[:5]                                      # Get 5 posts containing title 'poe'
    template_name = 'posts/post_list.html'                                                          # Specify your own template name/location


class PostDetailView(generic.DetailView):
    model = Post