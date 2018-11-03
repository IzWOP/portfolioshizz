from django.shortcuts import render, get_object_or_404

from .models import Post
def blogposts(request):
	post = Post.objects
	return render(request, 'blog/posts.html', {'post':post, 'title': 'Posts'})

def detail(request, blog_id):
	detailblog = get_object_or_404(Post, pk=blog_id)
	return render(request, 'blog/detail.html',{'blog':detailblog})

