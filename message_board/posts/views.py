from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here
# function-based view
# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, "post_list.html", {"posts": posts})

class PostList(ListView):
    model = Post
    template_name = "post_list.html"