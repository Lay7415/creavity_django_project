from django.shortcuts import render, HttpResponse
from . import models

# Create your views here.
def main(request):
  posts = models.Post.objects.all()
  return render(request, 'posts.html' , {'posts': posts})

def post(request, post_id):
    post = models.Post.objects.get(id=post_id)
    comments = models.Comment.objects.filter(post=post)
    
    return render(request, 'post.html', {'post': post, 'comments': comments})
