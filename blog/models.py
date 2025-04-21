from django.db import models
from django.urls import reverse

from django.db.models import UniqueConstraint                                   # Constrains fields to unique values
from django.db.models.functions import Lower                                    # Returns lower cased value of field


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        help_text="Enter a post category (e. g. News, Gaming etc.)"
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.id)])                  # Returns the url to access a particular genre instance.
    
    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='category_name_case_insensitive_unique',
                violation_error_message= "Category already exists (case insensitive match)"
            )
        ]


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author',on_delete=models.RESTRICT, null=True)
    body = models.TextField()
    category = models.ManyToManyField(Category, help_text="Select a category for this post")
    created_on = models.DateTimeField(auto_now_add=True)                        # auto_now_add assigns the current date whenever you create an instance of this class
    last_modified = models.DateTimeField(auto_now=True)                         # Whenever you edit an instance of this class, last_modified is updated

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])
    
    def display_category(self):
        return ', '.join(category.name for category in self.category.all()[:3])
    

    display_category.short_description = 'Category'


class Comment(models.Model):
    author = models.ForeignKey('Author',on_delete=models.RESTRICT, null=True)
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} on {self.post}"
    
    def get_absolute_url(self):
        return reverse('comment-detail', args=[str(self.id)])
    
    def display_body(self):
        return self.body[:30]
    

    display_body.short_description = 'View of Comment'


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
    
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])