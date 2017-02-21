from django.shortcuts import render, HttpResponse, redirect
from .models import Course, Description

def index(request):
    context = {
    "courses" : Course.objects.select_related("description_id").all(),
    "descriptions": Description.objects.all()
    }
    return render(request, "courses_app/index.html", context)

def process(request):
    x = Description.objects.create(description=request.POST['description'])
    Course.objects.create(name=request.POST['name'], description_id = x)
    print x.pk
    return redirect('/')

def confirm(request, id):
    holder = {
        "course_info" : Course.objects.select_related("description_id").get(id=id)
        # "course_descript" : Description.objects.get(description_id=id)
    }
    return render(request, "courses_app/confirm.html", holder)

def confirmed(request, id):
    ids = Course.objects.get(id=id).delete()
    return redirect("/")
