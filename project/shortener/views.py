from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Content
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import unquote

# Create your views here.


form = """
    This shortener URL does not exist in the data base.
    <p> Add a new URL for this shortener URL.
    <form action="" method="POST">
        <p>Insert URL: <input type="text" name="form_url"></p>
        <p><input type="submit" value="Send"></p>
    </form>
"""

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
        answer = "The URL is " + content.url + "\nThe short URL is " + content.shorturl + "\nThe ID is " + str(content.id)
    except Content.DoesNotExist:
        answer = form
    return HttpResponse(answer)
