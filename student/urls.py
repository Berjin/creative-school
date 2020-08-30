from django.urls import path
from .import views

urlpatterns = [
    path('',views.student,name="student"),
    path('attendance/',views.attendance, name='attendance'),
    path('contact/',views.contact, name='contact'),
    path('timetable/',views.timetable, name='timetable'),
    path('progress/',views.progress, name='progress'),
    path('homework/',views.homework, name='homework'),
    path('notice/',views.notice, name='notice'),
    path('material/',views.material,name='material')

]