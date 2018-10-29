from django.shortcuts import render

from .models import Post
def blogposts(request):
	post = Post.objects
	return render(request, 'blog/posts.html', {'post':post})
