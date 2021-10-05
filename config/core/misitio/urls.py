from django.urls import path
from core.misitio.views.actareuniones.views import ActaReunListView, ActaReunCreateView
from core.misitio.views.evaluaciones.views import EvaluacionListView, EvaluacionCreateView, EvaluacionUpdateView, EvaluacionDeleteView

app_name = 'core.misitio'
urlpatterns = [
    # evaluaciones
    path('evaluaciones/listar/', EvaluacionListView.as_view(), name='evaluaciones_listar'),
    path('evaluaciones/crear/', EvaluacionCreateView.as_view(), name='evaluaciones_crear'),
    path('evaluaciones/editar/<int:pk>/', EvaluacionUpdateView.as_view(), name='evaluaciones_editar'),
    path('evaluaciones/eliminar/<int:pk>/', EvaluacionDeleteView.as_view(), name='evaluaciones_eliminar'),

    # actareun
    path('actareun/listar/', ActaReunListView.as_view(), name='actareu_listar'),
    path('actareun/crear/', ActaReunCreateView.as_view(), name='actareu_crear'),

]
