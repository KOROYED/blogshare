from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import Post, Category, Comment
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from .forms import SignUpForm, CommentForm, CreatePostForm

def blog_index(request):
    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits

    context = {
        'num_visits': num_visits,
    }
    return render(request, "blog/index.html", context=context)


class PostByCategoryListView(generic.ListView):
    model = Post
    template_name = 'blog/category.html'
    
    def get_queryset(self):
        self.category = get_object_or_404(Category, name=self.kwargs["category"])
        return Post.objects.filter(category=self.category).order_by('-created_on')
    
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
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = self.request.user
            comment.save()
            return redirect(self.object.get_absolute_url())
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)


class CreatePost(generic.CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = "blog/create_post.html"
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AuthorListView(generic.ListView):
    model = User
    context_object_name = "author_list"
    template_name = 'blog/author_list.html'


class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'blog/author_detail.html'


class AuthorPostListView(generic.ListView):
    model = Post
    template_name = 'blog/author_post_list.html'
    
    def get_queryset(self):
        self.author = get_object_or_404(User, pk=self.kwargs["pk"])
        return Post.objects.filter(author=self.author).order_by('-created_on')
    
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
        self.author = get_object_or_404(User, pk=self.kwargs["pk"])
        return Comment.objects.filter(author=self.author).order_by('-created_on')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["author"] = self.author
        return context


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"




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