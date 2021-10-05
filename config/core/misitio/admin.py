from django.contrib import admin
from core.misitio.models import *
# Register your models here.
admin.site.register(Evaluacion)
fields = ('ename', 'eapellido', 'eedad', 'egrupo', 'Anno_Academic', 'emilitancia', 'eautoevaluacion', 'evaluacion')
radio_fields = {'emilitancia':admin.HORIZONTAL}                
admin.site.register(EventEstudiant)
admin.site.register(ActaReun)