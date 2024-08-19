from django.db import models

from django.contrib.auth.models import AbstractUser

from django.template.defaultfilters import slugify
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=225, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=225, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="BlogPhotos/", null=True, blank=True)
    user = models.ForeignKey("folio.User", on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse("single", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.title)
            
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class User(AbstractUser):
    profile_photo = models.ImageField(upload_to="ProfilePhotos/", null=True, blank=True)
    biography = models.CharField(max_length=225, null=True, blank=True)
    work = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.username
        

class Comment(models.Model):    
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=225, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    web_site = models.URLField(unique=True, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    title = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.title
    

class Portfolio(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="PortfolioPhotos/", null=True, blank=True)

    def __str__(self):
        return f"{self.category}"
    

class GetInTouch(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    subject = models.CharField(max_length=225, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    