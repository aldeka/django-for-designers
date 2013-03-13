from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from bookmarks.models import Bookmark, Tag
from bookmarks.forms import BookmarkForm

 
def index(request):
    if request.method == "POST":
        form = BookmarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    bookmarks = Bookmark.objects.all().order_by('-timestamp')[:10]
    current_user = request.user
    form = BookmarkForm(initial={'author': current_user})
    context = {
        'bookmarks': bookmarks,
        'form': form,
    }
    return render(request, 'index.html', context)


def tag(request, tag_name):
    tag = get_object_or_404(Tag, slug=tag_name)
    bookmarks = tag.bookmarks.all()
    context = {
        'tag': tag,
        'bookmarks': bookmarks,
    }
    return render(request, 'tag.html', context)