from django.shortcuts import render

from .models import Weight
from .forms import WeightForm


def testing(request):
    form = WeightForm(request.POST or None)

    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'weightpage/formtesting.html', context)


def displayweight(request):
    list_of_past_weight = Weight.objects.all()
    output = [w.weight for w in list_of_past_weight]
    return render(request, 'weightpage/weightpage.html', {
        'weights': output
    })
