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
    weight = [(w.weight, w.time.strftime("%H:%M"), w.time.strftime("%m/%d/%Y")) for w in list_of_past_weight]


    form = WeightForm(request.POST or None)

    if form.is_valid():
        form.save()


    context = {
        'weights': weight,
        'form': form
    }

    return render(request, 'weightpage/weightpage.html', context)
