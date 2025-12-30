from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# NOTE: Views can be created as class or function based on "music_controller\music_controller\urls.py" (?)

def main(request):
    return HttpResponse("<h1> Hello the endpoint is working </h1>")