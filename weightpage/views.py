from django.shortcuts import render

from .models import Weight


# Create your views here.
def displayweight(request):
    list_of_past_weight = Weight.objects.all()
    output = [w.weight for w in list_of_past_weight]
    return render(request, 'weightpage/weightpage.html', {
        'weights': output
    })
