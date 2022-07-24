from urllib import response
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    data = {
        'host': request.headers['Host'],
        'connection': request.headers['Connection'],
        'user_agent': request.headers['User-Agent'],
        'session': request.session,
        'user': request.user
    }

    return render(request, 'django_headers/index.html', data)