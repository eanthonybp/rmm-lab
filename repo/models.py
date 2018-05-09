from __future__ import unicode_literals
from django.db import models
from datetime import datetime


# Create your models here.
class Post(models.Model):
    email_contact = models.EmailField(max_length=75)
    author = models.ForeignKey('Author')
    title = models.CharField(max_length=75)
    snippet = models.TextField()
    description = models.TextField()
    category = models.ForeignKey('Category')
    created = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.email_contact + " : " + self.biggest_problem
        
class Category(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name
        
class Author(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    def __str__(self):
        return self.name
        
class Comment(models.Model):
    comment = models.TextField()
    snippet = models.TextField()
    post = models.ForeignKey('Post')
    author = models.ForeignKey('Author')
    def __str__(self):
        return self.author