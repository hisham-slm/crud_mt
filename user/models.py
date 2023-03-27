from django.db import models

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey('common.User',on_delete=models.CASCADE)
    post = models.CharField(max_length=20000)
    status = 'pending'
    votes = models.IntegerField()
    status = models.CharField(max_length=10)

    class Meta():
        db_table = 'post'

class LikedPosts(models.Model):
    user = models.ForeignKey('common.User',on_delete= models.CASCADE)
    post = models.ForeignKey('Post',on_delete= models.CASCADE)

    class Meta():
        db_table = 'liked_posts'