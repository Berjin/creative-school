from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from datetime import date
from .filters import AttendanceFilter
import datetime
# Create your views here

def attendance(request):
    if request.user.is_authenticated:
        days = Attendance.objects.filter(user=request.user).order_by('-date')
        myFilter = AttendanceFilter(request.GET,queryset=days)
        days = myFilter.qs[:8]
        today = date.today()
        context = {'days':days,'today':today,'myFilter':myFilter}
        return render(request,'attendance.html',context)
    return render(request,'attendance.html')
    
def student(request):
    if request.user.is_authenticated:
        details = StudentProfile.objects.filter(user=request.user)
        return render(request,'student.html',{'details':details})
    elif not request.user.is_authenticated:
        return redirect('login')
    return render(request,'student.html')

def contact(request):
    if request.user.is_authenticated:
        managers = ManagementContact.objects.all()
        standard = StudentProfile.objects.get(user=request.user).standard
        teachers = Teachers.objects.filter(standard__standard=standard)
        context = {'managers':managers,'teachers':teachers}
        return render(request,'contact.html',context)
    return render(request,'contact.html')

def timetable(request):
    if request.user.is_authenticated:
        standard = StudentProfile.objects.get(user=request.user).standard
        periods = Timetable.objects.filter(standard__standard=standard)
        context = {'periods':periods}
        return render(request,'timetable.html', context)
    return render(request,'timetable.html')

def progress(request):
    return render(request,'progress.html')

def homework(request):
    if request.user.is_authenticated:
        standard = StudentProfile.objects.get(user=request.user).standard
        subjects = Subject.objects.filter(standard__standard=standard)
        works = HomeWork.objects.filter(standard__standard=standard).distinct('subject')
        modals = HomeWork.objects.filter(standard__standard=standard)
        context = {'subjects':subjects,'works':works,'modals':modals}
        return render(request,'homework.html',context)
    return render(request,'homework.html')

def notice(request):
    if request.user.is_authenticated:
        importants = Notice.objects.filter(important=True).order_by('-datetime')
        notices = Notice.objects.all().order_by('-datetime')
        context = {'importants':importants,'notices':notices}
        return render(request,'notice.html', context)
    return render(request,'notice.html')

def material(request):
    standard = StudentProfile.objects.get(user=request.user).standard
    materials = Material.objects.filter(standard=standard)
    list1 =[]
    for i in materials:
        
        if i.url:
            x = i.url[17:]
            if x:
                i.url = '<iframe class="embed-responsive-item" src="https://www.youtube-nocookie.com/embed/'+x+' " frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    return render(request,'material.html',{'materials':materials})
