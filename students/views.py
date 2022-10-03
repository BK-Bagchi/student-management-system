from django.shortcuts import render
from .models import *


def index(request):
    students = Student.objects.all()
    return render(request, 'students/index.html', context={'students': students})
