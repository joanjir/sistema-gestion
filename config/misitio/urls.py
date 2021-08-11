from django.urls import path
from misitio.views.evaluaciones.views import *

app_name = 'misitio'
urlpatterns = [
    # evaluaciones
    path('evaluaciones/listar/', EvaluacionListView.as_view(), name='evaluaciones_listar'),
]
