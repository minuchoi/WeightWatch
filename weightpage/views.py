from django.shortcuts import render, Http404

from .models import Weight, SideBar
from .forms import WeightForm


def dashboard(request, variable):
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

    elif variable == "analytics":
        list_of_past_weight = Weight.objects.all()
        weight = [(w.weight, w.time.strftime("%H:%M"), w.time.strftime("%m/%d/%Y")) for w in list_of_past_weight]

        sidebar = SideBar.objects.all()

        context = {
            'weights': weight,
            'sidebar': sidebar,
        }

        return render(request, 'weightpage/analytics.html', context)

    elif variable == "settings":
        return render(request, 'loginpage/loginpage.html')

    elif variable == "signout":
        return render(request, 'loginpage/loginpage.html')

    else:
        return render(request, 'loginpage/loginpage.html')




