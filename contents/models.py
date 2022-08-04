from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

def user_path(instance, filename):
    from random import choice
    import string

    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    extension = filename.split('.')[-1]

    return 'accounts/{}/{}.{}'.format(instance.user, pid, extension)

# Create your models here.
class NewPost(models.Model):
    user = models.TextField(max_length=40, null=True)
    date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=40, null=True)
    imgfile = ProcessedImageField(upload_to=user_path,
                                  format='JPEG', options={'quality': 90},
                                  blank=True)
    content = models.TextField(max_length=4000, null=True)