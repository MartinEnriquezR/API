from sistema.models import DispositivoRastreador
from django.core.management.base import BaseCommand

#librerias de python
import csv
from catalogo.models import *

#comando
class Command(BaseCommand):
    
    def handle(self,*args,**options):
        self.circunstancias()
        self.colorCabello()
        self.colorOjos()
        self.colorPiel()
        self.complexion()
        self.enfermedad()
        self.formaRostro()
        self.lazo()
        self.pais()
        self.senasParticulares()
        self.texturaCabello()
        self.tipoCejas()
        self.tipoNariz()
        self.ubicacionCorporal()
        self.estadoCivil()
        self.dispositivoRastreador()

    def circunstancias(self):

        cantidad = Circunstancia.objects.all().count()

        if cantidad != 0:    
            Circunstancia.objects.all().delete()
        
        path = 'ModelosCSV/Circunstancia.csv'
        with open(path) as csvfile:
            campos = csv.reader(csvfile,delimiter=',')
            for row in campos:
                Circunstancia.objects.create(tipo_circunstancia=row[0])

    def colorCabello(self):

        cantidad = ColorCabello.objects.all().count()
        
        if cantidad != 0:    
            ColorCabello.objects.all().delete()
        
        path = 'ModelosCSV/ColorCabello.csv'
        with open(path) as csvfile:
            campos = csv.reader(csvfile,delimiter=',')
            for row in campos:
                ColorCabello.objects.create(color_cabello=row[0])

    def colorOjos(self):

        cantidad = ColorOjos.objects.all().count()
        
        if cantidad != 0:    
            ColorOjos.objects.all().delete()
        
        path = 'ModelosCSV/ColorOjos.csv'
        with open(path) as csvfile:
            campos = csv.reader(csvfile,delimiter=',')
            for row in campos:
                ColorOjos.objects.create(color_ojo=row[0])

    def colorPiel(self):
        
        cantidad = ColorPiel.objects.all().count()
        
        if cantidad != 0:    
            ColorPiel.objects.all().delete()
        
        path = 'ModelosCSV/ColorPiel.csv'
        with open(path) as csvfile:
            campos = csv.reader(csvfile,delimiter=',')
            for row in campos:
                ColorPiel.objects.create(color_piel= row[0])

    def complexion(self):

        cantidad = Complexion.objects.all().count()

        if cantidad != 0:    
            Complexion.objects.all().delete()

        path = 'ModelosCSV/Complexion.csv'
        with open(path) as csvfile:
            campos = csv.reader(csvfile,delimiter=',')
            for row in campos:
                Complexion.objects.create(complexion= row[0])
    
    def enfermedad(self):

        cantidad = Enfermedad.objects.all().count()
        
        if cantidad != 0:    
            Enfermedad.objects.all().delete()
        
        path = 'ModelosCSV/Enfermedad.csv'
        with open(path) as csvfile:
            campos = csv.reader(csvfile,delimiter=',')
            for row in campos:
                Enfermedad.objects.create(nombre_enfermedad=row[0])

    def formaRostro(self):

        cantidad = FormaRostro.objects.all().count()
        
        if cantidad != 0:    
            FormaRostro.objects.all().delete()
        
        path = 'ModelosCSV/FormaRostro.csv'
        with open(path) as csvfile:
            campos = csv.reader(csvfile,delimiter=',')
            for row in campos:
                FormaRostro.objects.create(forma_rostro=row[0])

    def lazo(self):
        
        cantidad = Lazo.objects.all().count()
        
        if cantidad != 0:    
            Lazo.objects.all().delete()
        
        path = 'ModelosCSV/Lazo.csv'
        with open(path) as csvfile:
            campos = csv.reader(csvfile,delimiter=',')
            for row in campos:
                Lazo.objects.create(lazo=row[0])

    def pais(self):

        cantidad = Pais.objects.all().count()
        
        if cantidad != 0:    
            Pais.objects.all().delete()
        
        path = 'ModelosCSV/Pais.csv'
        with open(path) as csvfile:
            campos = csv.reader(csvfile,delimiter=',')
            for row in campos:
                Pais.objects.create(nombre_pais=row[0],nacionalidad=row[1])

    def senasParticulares(self):
        
        cantidad = SenasParticulares.objects.all().count()
        if cantidad != 0:    
            SenasParticulares.objects.all().delete()

        path = 'ModelosCSV/SenasParticulares.csv'
        with open(path) as csvfile:
            campos = csv.reader(csvfile,delimiter=',')
            for row in campos:
                SenasParticulares.objects.create(nombre_sena_particular=row[0])

    def texturaCabello(self):
        
        cantidad = TexturaCabello.objects.all().count()
        
        if cantidad != 0:    
            TexturaCabello.objects.all().delete()
        
        path = 'ModelosCSV/TexturaCabello.csv'
        with open(path) as csvfile:
            campos = csv.reader(csvfile,delimiter=',')
            for row in campos:
                TexturaCabello.objects.create(textura_cabello = row[0])

    def tipoCejas(self):

        cantidad = TipoCejas.objects.all().count()
        
        if cantidad != 0:    
            TipoCejas.objects.all().delete()
        
        path = 'ModelosCSV/TipoCejas.csv'
        with open(path) as csvfile:
            campos = csv.reader(csvfile,delimiter=',')
            for row in campos:
                TipoCejas.objects.create(tipo_ceja=row[0])

    def tipoNariz(self):
        
        cantidad = TipoNariz.objects.all().count()
        
        if cantidad != 0:    
            TipoNariz.objects.all().delete()
        
        path = 'ModelosCSV/TipoNariz.csv'
        with open(path) as csvfile:
            campos = csv.reader(csvfile,delimiter=',')
            for row in campos:
                TipoNariz.objects.create(tipo_nariz=row[0])

    def ubicacionCorporal(self):

        cantidad = UbicacionCorporal.objects.all().count()
        
        if cantidad != 0:    
            UbicacionCorporal.objects.all().delete()
        
        path = 'ModelosCSV/UbicacionCorporal.csv'
        with open(path) as csvfile:
            campos = csv.reader(csvfile,delimiter=',')
            for row in campos:
                UbicacionCorporal.objects.create(nombre_ubicacion_corporal=row[0])

    def estadoCivil(self):
        
        cantidad = EstadoCivil.objects.all().count()
        
        if cantidad != 0:    
            EstadoCivil.objects.all().delete()
        
        path = 'ModelosCSV/EstadoCivil.csv'
        with open(path) as csvfile:
            campos = csv.reader(csvfile,delimiter=',')
            for row in campos:
                EstadoCivil.objects.create(estado_civil=row[0])
    
    def dispositivoRastreador(self):
        #direccion del archivo
        path = 'ModelosCSV/DispositivoRastreador.csv'

        #lista de 1000 numeros
        dispositivos = list(range(1,1001))
        
        #llenar el csv con los dispositivos
        with open(path,'w') as file:
            wr = csv.writer(file,delimiter='\n')
            wr.writerow(dispositivos)

        #verificar que no existan registros
        cantidad = DispositivoRastreador.objects.all().count()
        
        if cantidad != 0:    
            DispositivoRastreador.objects.all().delete()

        with open(path) as csvfile:
            campos = csv.reader(csvfile,delimiter=',')
            for row in campos:
                DispositivoRastreador.objects.create(numero_serie=row[0])