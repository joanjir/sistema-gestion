from datetime import datetime
from django import forms
from django.forms import ModelForm

from core.misitio.models import Evaluacion, ActaReun


class EvaluacionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EvaluacionForm, self).__init__(*args, **kwargs)
        self.fields['ename'].widget.attrs['autofocus'] = True

    class Meta:
        model = Evaluacion
        fields = 'ename', 'eapellido', 'eedad', 'egrupo', 'Anno_Academic', 'emilitancia', 'eautoevaluacion', 'evaluacion'

        widgets = {
            'ename': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese los nombres',

                }
            ),

            'eapellido': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese los apellidos',

                }),

            'eedad': forms.NumberInput(
                attrs={
                    'placeholder': 'Ingrese la edad',

                }),
            'egrupo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el grupo',

                }),
            'Anno_Academic': forms.Select(
                attrs={
                    'placeholder': 'Ingrese el año academico',

                }),
            'emilitancia': forms.Select(
                attrs={
                    
                }),
            'eautoevaluacion': forms.Textarea(
                attrs={
                    'placeholder': 'Ingrese autoevaluación',

                }),
            'evaluacion': forms.Select(
                attrs={

                }),



        }
        


    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class ActaReunForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['acgrupo'].widget.attrs['autofocus'] = True

    class Meta:
        model = ActaReun
        fields = '__all__'
        widgets = {
            'acgrupo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el grupo',
                }
            ),
            'acfecha': forms.DateTimeInput(format='%Y-%m-%d',
                                       attrs={
                                           'value': datetime.now().strftime('%Y-%m-%d'),
                                       }
                                       ),

            'acasistencia': forms.NumberInput(
                attrs={
                    'placeholder': 'Ingrese la  asistencia',
                }
            ),
            'acresumen': forms.Textarea(
                attrs={
                    'placeholder': 'Ingrese un resumen de la reunión',

                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
