import django_filters
from .models import *

class AttendanceFilter(django_filters.FilterSet):
    class Meta:
        model = Attendance
        fields = ['date']