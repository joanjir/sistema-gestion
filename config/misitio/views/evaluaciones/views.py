

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from misitio.models import Evaluacion


class EvaluacionListView(ListView):
    model= Evaluacion
    template_name='evaluaciones/listarevaluaciones.html'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['title'] = 'Listado de Evaluaciones'
        return context