from django.shortcuts import render
import os.path

from .models import UserDetail


# Create your views here.
def displaylogin(request):
    user_info = UserDetail.objects.all()
    return render(request, 'loginpage/loginpage.html', {
        'user_info': user_info
    })
