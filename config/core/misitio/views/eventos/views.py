from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.misitio.models import  EventEstudiant




class EventoListView(ListView):
    model = EventEstudiant
    template_name = 'eventos/listarevento.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        

        return context

