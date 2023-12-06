from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm

# Create your views here.
def homePage(request):
    form = StudentForm
    if request.method == "POST":
        form = StudentForm(request.POST,request.FILES)
        form.save()
        form = StudentForm

    data = Student.objects.all()
    context = {
        'form':form,
        'data':data
    }
    return render(request,"homePage.html",context)

def deletePage(request):
    return render(request,"deletePage.html",)
    

def updatePage(request):
    return render(request,"updatePage.html",)
    
