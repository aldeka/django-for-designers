from django.db import models

class Bookmark(models.Model):
    url = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, blank=True, default="")
    
    
class Tag(models.Model):
    bookmarks = models.ManyToManyField(Bookmark)
    slug = models.CharField(max_length=50, unique=True)