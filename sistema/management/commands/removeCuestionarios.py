from django.core.management.base import BaseCommand
from sistema.models import Cuestionario

class Command(BaseCommand):

    def handle(self,*args,**options):
        
        #remover a todos los cuestionarios de la base de datos
        cuestionarios = Cuestionario.objects.all().delete()