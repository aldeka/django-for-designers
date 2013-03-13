from django.http import HttpResponse

 
def index(request):
    return HttpResponse("Hello, world. You're at the bookmarks index.")


def tag(request, tag_name):
    return HttpResponse("This is a tag: <strong>%s</strong>" % (tag_name,))
    