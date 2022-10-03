from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    students = Student.objects.all()
    return render(request, 'students/index.html', context={'students': students})


def view_student(request, id):
    students = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))
