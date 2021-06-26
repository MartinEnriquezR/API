from django.core.management.base import BaseCommand
from sistema.models import Persona

class Command(BaseCommand):

    def handle(self, *args, **options):
        if not Persona.objects.filter(username='admin').exists():
            
            Persona.objects.create_superuser(
                username = 'admin',
                email = 'jmeenriquezr@gmail.com',
                nombre = 'Jose Martin',
                apellido_paterno = 'Enriquez',
                apellido_materno = 'Rodriguez',
                genero = 'Masculino',
                fecha_nacimiento = '1997-03-18',
                is_usuaria = False,
                is_contacto_confianza = True,
                password = '3d23d234f3',
            )