from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import MMRmodel


# Create your views here.
def index(request):
    mmrdata = MMRmodel.objects.all()

    context = {

    }
    return render(request, 'index.html', context)
