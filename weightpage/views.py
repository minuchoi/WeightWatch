from django.shortcuts import render

from .models import Weight, SideBar
from .forms import WeightForm


def testing(request):
    form = WeightForm(request.POST or None)

    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'weightpage/formtesting.html', context)


def displayweight(request, variable):
    if variable == "home":
        list_of_past_weight = Weight.objects.all()
        weight = [(w.weight, w.time.strftime("%H:%M"), w.time.strftime("%m/%d/%Y")) for w in list_of_past_weight]

        form = WeightForm(request.POST or None)

        if form.is_valid():
            form.save()

        sidebar = SideBar.objects.all()

        context = {
            'weights': weight,
            'form': form,
            'sidebar': sidebar,
        }

        return render(request, 'weightpage/weightpage.html', context)

    else:
        return render(request, 'loginpage/loginpage.html')




