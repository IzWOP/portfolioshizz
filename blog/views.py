from django.shortcuts import render


def blogposts(request):
	return render(request, 'blog/posts.html')
