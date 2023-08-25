from django.db import models
from django.utils.text import slugify
# from django.core.validators import MinValueValidator,MaxValueValidator



# Create your models here.


class Post(models.Model):
    course_name = models.CharField(max_length=50)
    develop_by = models.CharField(max_length=50)
    release_date= models.DateTimeField(auto_now=True)
    # course_title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=400)    
    content = models.CharField(max_length=500)
    course_image = models.ImageField(upload_to="posts")
    course_slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.course_slug = slugify(self.course_name)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.course_name}"



