from django.http import HttpResponse
from django.shortcuts import render
from bookmarks.models import Bookmark, Tag

 
def index(request):
    bookmarks = Bookmark.objects.all().order_by('-timestamp')[:10]
    context = {
        'bookmarks': bookmarks,
    }
    return render(request, 'index.html', context)


def tag(request, tag_name):
    tag = Tag.objects.get(slug=tag_name)
    bookmarks = tag.bookmarks.all()
    context = {
        'tag': tag,
        'bookmarks': bookmarks,
    }
    return render(request, 'tag.html', context)