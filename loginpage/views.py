from django.shortcuts import render
import os.path

from .models import UserDetail
from .forms import RegisterForm


# Create your views here.
def displaylogin(request):
    user_info = UserDetail.objects.all()
    return render(request, 'loginpage/loginpage.html', {
        'user_info': user_info
    })


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, '')
    else:
        form = RegisterForm()

    return render(request, 'loginpage/register.html', {'form': form})
