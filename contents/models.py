from django.db import models

# Create your models here.
class NewPost(models.Model):
    user = models.TextField(max_length=40, null=True)
    date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=40, null=True)
    imgfile = models.ImageField(null=True, upload_to="", blank=True)
    content = models.TextField(max_length=4000, null=True)