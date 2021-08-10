




from django.views.generic import ListView
from misitio.models import Evaluacion


class EvaluacionListView(ListView):
    model= Evaluacion
    #template_name