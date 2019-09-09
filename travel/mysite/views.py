from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views import generic
# Create your views here.
def index(request):
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(request, 'index.html', context={ 'num_visits': num_visits})

