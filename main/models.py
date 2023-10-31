from django.db import models

class User(models.Model):
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/posts/{self.id}'
    
class Comment(models.Model):
    description = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

