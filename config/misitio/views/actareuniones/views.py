from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from misitio.models import ActaReun

from misitio.form import ActaReunForm


class ActaReunListView(ListView):
    model = ActaReun
    template_name = 'actasreuniones/listaractasreu.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in ActaReun.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Actas de Reuniones'
        context['create_url'] = reverse_lazy('misitio:actareu_crear')

        return context


class ActaReunCreateView(CreateView):
    model = ActaReun
    form_class = ActaReunForm
    template_name = 'actasreuniones/crearactareu.html'
    success_url = reverse_lazy('misitio: actareu_listar')
    permission_required = 'actareu_crear'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Acta de Reunión'
        context['entity1'] = 'Evaluaciones Integrales'
        context['entity2'] = 'Evaluaciones Integrales'
        context['list_url'] = reverse_lazy('misitio:evaluaciones_listar')
        context['action'] = 'add'
        return context
