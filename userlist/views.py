from django.shortcuts import render
from django.http import HttpResponse
from .models import Member


def index(request):
    members = Member.objects.all()
    return render(request, 'index.html', {'members': members})


