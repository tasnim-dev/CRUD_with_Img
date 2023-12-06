from django.db import models


# Create your models here.

class Student(models.Model):
    Student_name = models.CharField(max_length=20,null=True)
    Department = models.CharField(max_length=20,null=True)
    Phone = models.CharField(max_length=20,null=True)
    Joinat = models.DateTimeField(auto_now_add=True)
    Profile_img = models.ImageField(upload_to="ProfileImg",null=True, blank=True)

    def __str__(self):
        return self.Student_name
