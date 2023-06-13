from django.db import models

# Create your models here.
class BlogPost(models.Model):
    post_id =models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    head_0 = models.CharField(max_length=100 , default="")
    content_0 = models.CharField(max_length=10000, default="")
    head_1 = models.CharField(max_length=100, default="")
    content_1 = models.CharField(max_length=10000, default="")
    head_2 = models.CharField(max_length=100, default="")
    content_2 = models.CharField(max_length=10000, default="")
    head_3 = models.CharField(max_length=100, default="")
    content_3 = models.CharField(max_length=10000, default="")
    head_4 = models.CharField(max_length=100, default="")
    content_4 = models.CharField(max_length=10000, default="")
    publish_date =models.DateTimeField()
    thumbnail = models.ImageField(upload_to='blog/thumbnail',default="")
    image_0 = models.ImageField(upload_to='blog/images',default="")
    image_1 = models.ImageField(upload_to='blog/images',default="")
    image_2 = models.ImageField(upload_to='blog/images',default="")
    def __str__(self):
        return self.title

