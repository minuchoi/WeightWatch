from django import forms

from .models import Weight


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class WeightForm(forms.ModelForm):
    class Meta:
        model = Weight
        fields = [
            'user',
            'weight',
            'time',
            'date'
        ]
        widgets = {
            'user':forms.HiddenInput(),
            'time': TimeInput(),
            'date': DateInput()
        }
