from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#conider setting null=True
class Standard(models.Model):
    standard = models.CharField(max_length=5)
    def __str__(self):
        return self.standard
class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    standard = models.ForeignKey(Standard,on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=True)
    def __str__(self):
        return '{} - {}'.format(str(self.date),str(self.user))
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics',default='/pics/avatar.jpg')
    standard = models.ForeignKey(Standard,on_delete=models.CASCADE)
    admission_number = models.IntegerField()
    roll_number = models.IntegerField()
    date_of_birth = models.DateField()
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    phone_number = models.BigIntegerField()
    address = models.CharField(max_length=200)
    blood_group = models.CharField(max_length=50)
    email = models.EmailField()
    EMIS_number = models.BigIntegerField()
    def __str__(self):
        return self.name
class Subject(models.Model):
    subject = models.CharField(max_length=200)
    standard = models.ManyToManyField(Standard)
    image = models.ImageField(upload_to='pics',default='/pics/subject_default.jpg')
    def __str__(self):
        return self.subject
class HomeWork(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    standard = models.ManyToManyField(Standard)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    deadline = models.DateField()
    def __str__(self):
        return '{} - {}'.format(self.title,self.subject)
class ManagementContact(models.Model):
    position = models.CharField(max_length=20)
    image = models.ImageField(upload_to='pics',default='/pics/manager_default.jpg')
    name = models.CharField(max_length=30)
    phone = models.BigIntegerField()
    email = models.EmailField()
    def __str__(self):
        return self.position
class Teachers(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    standard = models.ManyToManyField(Standard)
    name = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    email = models.EmailField()
    def __str__(self):
        return '{} Teacher'.format(self.subject)
class Notice(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    important = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Day(models.Model):
    day = models.CharField(max_length=10)
    def __str__(self):
        return self.day

class Timetable(models.Model):
    day = models.ForeignKey(Day,on_delete=models.CASCADE)
    standard = models.ForeignKey(Standard,on_delete=models.CASCADE)
    period1 = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='1+')
    period2 = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='2+')
    period3 = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='3+')
    period4 = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='4+')
    period5 = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='5+')
    period6 = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='6+')
    period7 = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='7+')
    period8 = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='8+')
    def __str__(self):
        return '{}-{}'.format(self.standard,self.day)

class Material(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    standard = models.ManyToManyField(Standard)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teachers,on_delete=models.CASCADE)
    url = models.URLField(blank=True)
    video = models.FileField(upload_to='video',blank=True)
    datetime = models.DateField(auto_now=True)
    def __str__(self):
        return '{} {} {}'.format(self.subject,self.title,self.datetime)


