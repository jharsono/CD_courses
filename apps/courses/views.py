from django.shortcuts import render, redirect, HttpResponse
from .models import Course
from django.contrib import messages


def index(request):
    context={

            "courses": Course.objects.order_by("-created_at")
    }

    return render(request, 'courses/index.html', context)


def add(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
        print "added"
        return redirect('/')

def delete(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')

def confirm_delete(request, id):

    context = {
            "courses" : Course.objects.get(id=id)
    }
    return render(request, 'courses/delete.html', context)
