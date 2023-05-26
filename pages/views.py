from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse ("<h1>helo</h1>")
    return render (request, "home.html", {})
def contact_view(request, *args, ** kwargs):
    #return HttpResponse ("<h1>Contact Page</h1>")
    return render (request, "contact.html", {})
def about_view(request, *args, ** kwargs):
    my_context = {
        "title": "This is about us",
        #"my_text": "This is about us",
        "this_is_true":True,
        "my_number": 123,
        "my_list": [123,654,879,'Abc'],
        "my_html": "<h1>hi</h1>",
    }

    #return HttpResponse ("<h1>About Page</h1>")
    return render (request, "about.html", my_context)
def social_view(request, *args, ** kwargs):
    #return HttpResponse ("<h1>Social Page</h1>")
    return render (request, "social.html", {})