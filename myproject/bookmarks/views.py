from django.http import HttpResponse
from django.shortcuts import render

 
def index(request):
    context = {}
    return render(request, 'index.html', context)


def tag(request, tag_name):
    return HttpResponse("This is a tag: <strong>%s</strong>" % (tag_name,))
    