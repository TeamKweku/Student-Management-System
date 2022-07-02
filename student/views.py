from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Student

# Create your views here.
def index(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'students/index.html', context)


def view_student(request, id):
    student = student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))