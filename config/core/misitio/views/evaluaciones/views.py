from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.misitio.models import Evaluacion

from core.misitio.form import EvaluacionForm


class EvaluacionListView(ListView):
    model = Evaluacion
    template_name = 'evaluaciones/listarevaluaciones.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Evaluacion.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Evaluaciones integrales'
        context['titlehead'] = 'Listado de Evaluaciones integrales | Sistema Gestión de la FEU Fac 2'

        context['create_url'] = reverse_lazy('core.misitio:evaluaciones_crear')

        return context


class EvaluacionCreateView(CreateView):
    model = Evaluacion
    form_class = EvaluacionForm
    template_name = 'evaluaciones/crearevaluacion.html'
    success_url = reverse_lazy('core.misitio:evaluaciones_listar')
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
        context['title'] = 'Crear Evaluación Integral'
        context['entity'] = 'Listado de Evaluaciones Integrales'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class EvaluacionUpdateView(UpdateView):
    model = Evaluacion
    form_class = EvaluacionForm
    template_name = 'evaluaciones/crearevaluacion.html'
    success_url = reverse_lazy('core.misitio:evaluaciones_listar')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Evaluacion Integral'
        context['entity'] = 'Evaluacion Integral'
        context['list_url'] = reverse_lazy('core.misitio:evaluaciones_listar')
        context['action'] = 'edit'
        return context
class EvaluacionDeleteView(DeleteView):
    model = Evaluacion
    template_name = 'evaluaciones/eliminarevaluacion.html'
    success_url = reverse_lazy('core.misitio:evaluaciones_listar')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Evaluación Integral'
        context['entity'] = 'Evalución Integral'
        context['list_url'] = reverse_lazy('core.misitio:evaluaciones_listar')
        return context