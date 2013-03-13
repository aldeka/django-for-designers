from django.db import models
from django.contrib.auth.models import User

class Bookmark(models.Model):
    author = models.ForeignKey(User)
    url = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, blank=True, default="")
    
    def __unicode__(self):
        return "%s by %s" % (self.url, self.author.username)
    
    
class Tag(models.Model):
    bookmarks = models.ManyToManyField(Bookmark)
    slug = models.CharField(max_length=50, unique=True)
    
    def __unicode__(self):
        return self.slug