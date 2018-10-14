from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, render_to_response


def gallery(request):
    return render_to_response("gallery.html")
#def about(request):
    #return render_to_response("about.html")

# Create your views here.
