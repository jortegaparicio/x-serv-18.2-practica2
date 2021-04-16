from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Content
# Create your views here.


def get_content(request, surl):
    try:
        content = Content.objects.get(shorturl=surl)
        answer = "The URL is " + content.url + "\nThe short URL is " + content.shorturl + "\nThe ID is " + str(content.id)
    except Content.DoesNotExist:
        raise Http404("It does not exist")
    return HttpResponse(answer)
