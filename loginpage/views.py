from django.shortcuts import render


# Create your views here.
def displaylogin(request):
    return render(request, 'loginpage/loginpage.html')
