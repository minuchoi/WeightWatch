from django.shortcuts import render, Http404

from .models import Weight, SideBar
from .forms import WeightForm

from datetime import datetime as dt


def dashboard(request, variable, message=None):
    sidebar = SideBar.objects.all()

    if variable == "home":
        form = WeightForm(request.POST or None,
                          initial={'user': 1, 'time': dt.now().strftime("%H:%M"), 'date': dt.now()})

        context = {
            'form': form,
            'sidebar': sidebar
        }

        if form.is_valid():
            form.save()
            context['message'] = "Data successfully inputted!"
            return render(request, 'weightpage/weightpage.html', context)

        else:
            context['message'] = None
            return render(request, 'weightpage/weightpage.html', context)

    elif variable == "analytics":
        list_of_past_weight = Weight.objects.all()
        weight = [(w.weight, w.time.strftime("%H:%M"), w.date.strftime("%d/%m/%Y"), w.id) for w in list_of_past_weight]

        context = {
            'weights': weight,
            'sidebar': sidebar,
            'message': message,
        }

        return render(request, 'weightpage/analytics.html', context)

    elif variable == "settings":
        return render(request, 'loginpage/loginpage.html')

    elif variable == "signout":
        return render(request, 'loginpage/loginpage.html')

    else:
        return render(request, 'loginpage/loginpage.html')


def edit_info(request, weight_id):
    sidebar = SideBar.objects.all()
    try:
        weight = Weight.objects.get(id=weight_id)

        form = WeightForm(instance=weight)

        context = {
            'form': form,
            'sidebar': sidebar,
            'weight': weight
        }

        if request.method == 'POST':
            new_form = WeightForm(request.POST, instance=weight)
            if new_form.is_valid():
                new_form.save()
                return dashboard(request, "analytics", message="Data successfully changed!")

        else:
            return render(request, 'weightpage/edit_info.html', context)

    except Weight.DoesNotExist:
        raise Http404('Data not found.')


def delete_data_page(request, weight_id):
    sidebar = SideBar.objects.all()

    try:
        chosen_weight = Weight.objects.get(id=weight_id)
        weight = (chosen_weight.weight, chosen_weight.time, chosen_weight.date, chosen_weight.id)
        context = {
            'sidebar': sidebar,
            'weight': weight
        }

        return render(request, 'weightpage/delete_info.html', context)

    except Weight.DoesNotExist:
        raise Http404('Data not found.')


def delete_data(request, weight_id):
    data = Weight.objects.get(id = weight_id)
    data.delete()
    return dashboard(request, "analytics", message="Data successfully deleted!")