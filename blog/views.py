from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post, Category, Author, Comment
from django.views import generic

def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")                                              # - in -created_on  reverses arrangment of objects by order_by
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context=context)


class PostByCategoryListView(generic.ListView):
    model = Post
    template_name = 'blog/category.html'
    
    def get_queryset(self):
        self.category = get_object_or_404(Category, name=self.kwargs["category"])
        return Post.objects.filter(category=self.category)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        return context
    

class PostListView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    paginate_by = 2
    ordering = ["-created_on"]


class PostDetailView(generic.DetailView):
    model = Post


class AuthorListView(generic.ListView):
    model = Author
    context_object_name = "author_list"


class AuthorDetailView(generic.DetailView):
    model = Author


class AuthorPostListView(generic.ListView):
    model = Post
    template_name = 'blog/author_post_list.html'
    
    def get_queryset(self):
        self.author = get_object_or_404(Author, pk=self.kwargs["pk"])
        return Post.objects.filter(author=self.author)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["author"] = self.author
        return context

class AuthorCommentListView(generic.ListView):
    model = Comment
    template_name = 'blog/author_comment_list.html'
    context_object_name = "comment_list"
    ordering = ["-created_on"]
    paginate_by = 10

    def get_queryset(self):
        self.author = get_object_or_404(Author, pk=self.kwargs["pk"])
        return Comment.objects.filter(author=self.author)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["author"] = self.author
        return context


# def blog_detail(request, pk):
#     post = Post.objects.get(pk=pk)                                                                  # pk = primary key
#     comments = Comment.objects.filter(post=post)
#     context = {
#         "post": post,
#         "comments": comments,
#     }
    
#     return render(request, "blog/detail.html", context)

# def blog_category(request, category):
#     posts = Post.objects.filter(category__name__contains = category).order_by("-created_on")        # category__name coz many to many field
#     context = {
#         "category": category,
#         "posts": posts,
#     }
#     return render(request, "blog/category.html", context=context)