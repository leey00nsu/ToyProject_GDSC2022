from django.db import models

# Create your models here.
class NewPost(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=40, null=True)
    imgfile = models.ImageField(null=True, upload_to="", blank=True)
    content = models.TextField(max_length=4000, null=True)