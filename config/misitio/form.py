from msilib import RadioButtonGroup
from datetime import datetime
from django.forms import *

from misitio.models import Evaluacion, ActaReun


class EvaluacionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EvaluacionForm, self).__init__(*args, **kwargs)
        self.fields['ename'].widget.attrs['autofocus'] = True


    class Meta:
        model = Evaluacion
        fields = 'ename', 'eapellido', 'eedad', 'egrupo', 'Anno_Academic', 'emilitancia', 'eautoevaluacion', 'evaluacion'

        widgets = {
            'ename': TextInput(
                attrs={
                    'placeholder': 'Ingrese los nombres',

                }
            ),

            'eapellido': TextInput(
                attrs={
                    'placeholder': 'Ingrese los apellidos',

                }),

            'eedad': NumberInput(
                attrs={
                    'placeholder': 'Ingrese la edad',

                }),
            'egrupo': TextInput(
                attrs={
                    'placeholder': 'Ingrese el grupo',

                }),
            'Anno_Academic': Select(
                attrs={
                    'placeholder': 'Ingrese el año academico',

                }),
            'emilitancia': Select(
                attrs={
                    'placeholder': 'Ingrese el año academico',
                }),
            'eautoevaluacion': Textarea(
                attrs={
                    'placeholder': 'Ingrese autoevaluación',

                }),
            'evaluacion': Select(
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
            'acgrupo': TextInput(
                attrs={
                    'placeholder': 'Ingrese el grupo',
                }
            ),
            'acfecha': DateInput(format='%Y-%m-%d',
                                 attrs={
                                     'value': datetime.now().strftime('%Y-%m-%d'),
                                 }
                                 ),
            'acasistencia': NumberInput(
                attrs={
                    'placeholder': 'Ingrese la  asistencia',
                }
            ),
            'acresumen': Textarea(
                attrs={
                    'placeholder': 'Ingrese un resumen de la reunión',
                    'rows': 3,
                    'cols': 3
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
