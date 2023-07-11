from django.shortcuts import render

from app.forms import *
# Create your views here.

from django.http import HttpResponse

def student_form(request):
    SFD=StudentForm()
    if request.method=='POST':
        SF=StudentForm(request.POST)
        if SF.is_valid():
            return HttpResponse(str(SFD.cleaned_data))
        else:
            return HttpResponse('data is not valid')
    return render(request,'Student_from.html',{'SFD':SFD})