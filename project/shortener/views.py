from django.shortcuts import render
from django.http import HttpResponse
from .models import Content
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import unquote
from django.template import loader

# Create your views here.

@csrf_exempt
def get_content(request, surl):
    # if the method is POST
    if request.method == "POST":
        # We are getting the data from HTTP body and we are saving it in the data base
        lurl = unquote(request.POST['form_url'])
        c = Content(url=lurl, shorturl=surl)
        # Here we add it in the data base
        c.save()

    # GET method, here we read it if it does exist, if it doesn't exist we give back a form
    try:
        content = Content.objects.get(shorturl=surl)
        answer = "The URL is " + content.url + "\nThe short URL is " + content.shorturl + "\nThe ID is " + \
                 str(content.id)
    except Content.DoesNotExist:
        template = loader.get_template('shortener/form.html')
        answer = template.render()
    return HttpResponse(answer)


def form_act(request):
    # We are getting the HTML
    template = loader.get_template('shortener/form.html')
    # We renderise this template
    return HttpResponse(template.render())
