from django.core.management.base import BaseCommand
from sistema.models import Persona,Cuestionario

class Command(BaseCommand):

    def handle(self,*args,**options):
        
        #remover a todos los usuarios de la base de datos
        persona = Persona.objects.all().delete()
        
        #remover cuestionarios
        cuestionarios = Cuestionario.objects.all().delete()