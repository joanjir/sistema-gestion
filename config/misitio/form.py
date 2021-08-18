from msilib import RadioButtonGroup

from django.forms import *



from misitio.models import Evaluacion


class EvaluacionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EvaluacionForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Evaluacion
        fields = '__all__'

        widgets = {
            'ename': TextInput(
                attrs={
                    'label':'',
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
