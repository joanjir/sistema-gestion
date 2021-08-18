from django.db import models
from django.forms import model_to_dict

# Create your models here.


class Evaluacion(models.Model):
    ename = models.CharField(max_length=30, verbose_name='Nombres')
    eapellido = models.CharField(max_length=30, verbose_name='Apellidos')
    eedad = models.PositiveIntegerField(verbose_name='Edad')
    egrupo = models.CharField(max_length=20, verbose_name='Grupo')
    Anno_Academics = (
        ('1er', 'Primero'),
        ('2do', 'Segundo'),
        ('3er', 'Tercero'),
        ('4to', 'Cuarto'),
        ('5to', 'Quinto'),
    )
    Anno_Academic = models.CharField(
        max_length=10, choices=Anno_Academics, verbose_name='Año Academico')
    MILITANCIA = (
        ('No', 'no'),
        ('Si', 'si'),
    )
    emilitancia = models.CharField(
        max_length=2, choices=MILITANCIA, verbose_name='Militancia')
    eautoevaluacion = models.TextField(
        verbose_name='Autoevaluación')
    EVALUACIONES = (
        ('B', 'Bien'),
        ('R', 'Regular'),
        ('M', 'Mal'),
    )
    evaluacion = models.CharField(
        max_length=1, choices=EVALUACIONES, verbose_name='Evaluación')

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta():
        verbose_name = 'Evaluacion Integral'
        verbose_name_plural = 'Evaluaciones Integrales'
        ordering = ['id']


class EventEstudiant(models.Model):
    evnombre = models.CharField(
        max_length=150, verbose_name='Nombre del Evento Estudiantil')
    evtipo = models.CharField(
        max_length=50, verbose_name='Tipo del Evento Estudiantil')
    evcantEstu = models.PositiveIntegerField(
        verbose_name='Cantidad del Estudiantes a Participar',     null=True)
    efecha = models.DateTimeField(
        null=True, verbose_name='Fecha del Evento Estudiantil')
    evlugar = models.CharField(
        max_length=100, verbose_name='Luga del Evento Estudiantil')

    class Meta():
        verbose_name = 'Evento Estudiantil'
        verbose_name_plural = 'Eventos Estudiantiles'


class ActaReun(models.Model):
    acgrupo = models.CharField(max_length=30, verbose_name='Grupo')
    acfecha = models.DateField(
        null=True, verbose_name='Fecha de Acta de Reunión')
    acasistencia = models.PositiveIntegerField(verbose_name='Asistecia')
    acresumen = models.TextField(verbose_name='Resumen')

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta():
        verbose_name = 'Acta de Reunion'
        verbose_name_plural = 'Actas de Reuniones'
