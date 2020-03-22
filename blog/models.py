from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

STATUS = (
    (0,"PUBLIC"),
    (1,"PRIVATE")
)
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True,blank=False)
    Description = models.TextField(blank=False)
    updated_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="uploads")
    status = models.IntegerField(choices=STATUS,default=0)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200,unique=True)
    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.title