from django.db import models

class Post(models.Model):
	image = models.ImageField(upload_to='blogimages/')
	title = models.CharField(max_length=100)
	body = models.TextField()
	time = models.DateTimeField(auto_created=True, auto_now=True)

	def __str__(self):
		return self.title
