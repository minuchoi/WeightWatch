from django.shortcuts import render


# Create your views here.
def displayweight(request):
    return render(request,'weightpage/weightpage.html')
