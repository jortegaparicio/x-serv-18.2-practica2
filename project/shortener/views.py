from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Content
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import unquote
from django.template import loader

# Create your views here.


@csrf_exempt
def get_content(request, surl):
    print("*******************************************************************+")
    if request.method == "POST":
        try:
            # We are getting the data from HTTP body and we are saving it in the data base
            short_url = unquote(request.POST['short'])
            long_url = unquote(request.POST['url'])
            c = Content(url=long_url, shortUrl=short_url)
            # Here we add it in the data base
            c.save()
        except Content.DoesNotExist:
            raise Http404("Recurso no disponible")

    # GET method, here we read it if it does exist, if it doesn't exist we give back a 404 error
    try:
        if surl is not None:
            # if the short url doesn't exist in our data base it will raise an exception
            content = Content.objects.get(shortUrl=surl)
            template = loader.get_template('shortener/redirection.html')
            print(content.url)
            c = {"content": content.url}
            answer = template.render(c)
        else:  # if the resource is /
            template = loader.get_template('shortener/form.html')
            answer = template.render()
    except Content.DoesNotExist:
        raise Http404("Recurso no disponible")
    return HttpResponse(answer)


def form_act(request):

    if request.method == "POST":
        short_url = unquote(request.POST['short'])
        long_url = unquote(request.POST['url'])
        if short_url == "" or long_url == "":  # if there is no QS
            raise Http404("No QS extracted from your form.")
        else:
            # We have to add 'https://' if the url doesn't have it
            if not long_url.startswith('http://') and not long_url.startswith('https://'):
                long_url = 'https://' + long_url
            # if this content exist we will delete from our data base
            exist = Content.objects.filter(shortUrl=short_url).exists()
            if exist:
                borr = Content.objects.get(shortUrl=short_url)
                borr.delete()
            c = Content(url=long_url, shortUrl=short_url) # Here we add the new content
            c.save()
        template = loader.get_template('shortener/posthtml.html')
        c = {"content": c}
        return HttpResponse(template.render(c))

    if request.method == "GET":
        contentlist = Content.objects.all()
        # We are getting the HTML
        template = loader.get_template('shortener/form.html')
        context = {
            'contentList': contentlist
        }
        # We renderise this template
        return HttpResponse(template.render(context, request))
