from django.contrib import admin
from .models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['Student_name', 'Department', 'Phone', 'Joinat', 'Profile_img']
