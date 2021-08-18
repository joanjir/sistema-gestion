from django.urls import path

from misitio.views.actareuniones.views import ActaReunListView

from misitio.views.evaluaciones.views import *


app_name = 'misitio'
urlpatterns = [
    # evaluaciones
    path('evaluaciones/listar/', EvaluacionListView.as_view(),
         name='evaluaciones_listar'),
    path('evaluaciones/crear/', EvaluacionCreateView.as_view(),
         name='evaluaciones_crear'),
    path('evaluaciones/editar/<int:pk>/',
         EvaluacionUpdateView.as_view(), name='evaluaciones_editar'),

    # actareun
    path('actareun/listar/', ActaReunListView.as_view(), name='actareu_listar'),
]
