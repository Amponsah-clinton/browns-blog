from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

class post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=300)
    snippet = models.CharField(max_length=100)
    post_category = models.ForeignKey(category, on_delete=models.CASCADE)
    details = RichTextField()
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    image = models.FileField(upload_to="images/", null=True, blank=True)
    link = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.title


class AddVideo(models.Model):
    title= models.CharField(max_length=200, default='Hi')
    snippet= models.CharField(max_length=200, default='Hi')
    link = models.URLField(max_length=200)
    image = models.ImageField(upload_to="images/")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date = models.DateField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return f"Video: {self.link}"


    
class contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=2000)

    def __str__(self):
        return self.name + " " + self.email


class advert(models.Model):
    ads_file = models.FileField(upload_to="images/", null=True, blank=True)




class comment(models.Model):
    posts = models.ForeignKey(post, on_delete=models.CASCADE, blank=True, null=True )
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(max_length=1200)

    def __str__(self):
        return self.name + " " + self.email 





