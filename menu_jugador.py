import time
import os
# DAOs
from Equipo.equipoDao import equipoDao
from Habilidades.habilidadesDao import habilidadesDao
from Personajes.personajesDao import personajesDao
from Poderes.poderesDao import poderesDao
from Razas.razasDao import razasDao


def pausarYvolver():
    print('1.- Volver: ')
    while(True):
        opcion = input('# ')
        if opcion == '1':
            return
        else:
            print('Valor Ingresado no Valido')

def obtenerRaza():
     # Obtener Raza del Personaje
    while(True):
        print('Ingrese la clase de su Personaje: ')
        print('1.- Humano')
        print('2.- Elfo')
        print('3.- Enano')
        print('4.- Mediano')
        raza = input('#: ')
        if raza < 1 or raza > 4:
            print('Valor Ingresado no Valido: '+raza)
        else:
            return

def crearPersonaje():
    os.system('cls')
    print('>> Creacion de Personaje >>')
    print('Ingrese el nombre de su Personaje: ')
    nombre = input('#: ')
    obtenerRaza()
    # Obtener atributos del peroanje
    while(True):
        print(
            'A continuacion posees 12 puntos a repartir entre los seis atributos del personaje: Fuerza, Destreza, Reistencia, Inteligencia, Sabiduria y Carisma'
        )
        fuerza = input('Fuerza: #: ')
        destreza = input('Destreza: #: ')
        resistencia = input('Resistencia: #: ')
        inteligencia = input('Inteligencia: #: ')
        sabiduria = input('Sabiduria: #: ')
        carisma = input('Carisma: #: ')
        total_puntos = fuerza+destreza+resistencia+inteligencia+sabiduria+carisma
        if (total_puntos) < 12:
            print(
                'No se distribuyeron correctamente los 12 puntos, por favor intentelo nuevamente')
        elif (total_puntos) > 12:
            print(
                'Ha ingresado mas puntos de los debidos, por favor distribuyalos nuevamente')
        else:
            return
    



# Menu ---------------------------------------->>


class menu_jugador():
    def __init__(self, enFuncionamiento, nombre):
        # imports Dao's
        equipo_dao = equipoDao()
        habilidad_dao = habilidadesDao()
        personaje_dao = personajesDao()
        poder_dao = poderesDao()
        raza_dao = razasDao()
        #
        while(enFuncionamiento):
            time.sleep(2)
            os.system('cls')
            print('<< Bienvenido Jugador: ' + nombre + ' >>')
            print(
                '<<------------------------------<< Menu >>------------------------------>>')
            print(
                'Seleccione que opcion desea ingresando el numero corrrespondiente a esta:')
            print('1.- Crear Personajes')
            print('2.- Ver Mis Personajes')
            print('3.- Razas')
            print('4.- Poderes')
            print('5.- Habilidades')
            print('6.- Equipos')
            print('7.- Salir')
            print(
                '<<------------------------------<< Menu >>------------------------------>>')
            seleccion = input('#: ')
            os.system('cls')
            if seleccion == '1':
                #crearPersonaje()
                r = raza_dao.obtenerRaza(81)
                print(r)
                pausarYvolver()
            elif seleccion == '2':
                pass
            elif seleccion == '3':
                raza_dao.mostrar()
                pausarYvolver()
            elif seleccion == '4':
                poder_dao.mostrar()
                pausarYvolver()
            elif seleccion == '5':
                habilidad_dao.mostrar()
                pausarYvolver()
            elif seleccion == '6':
                equipo_dao.mostrar()
                pausarYvolver()
            elif seleccion == '7':
                print('Hasta Luego ' + nombre)
                enFuncionamiento = False
            else:
                print('Valor Ingresado no Valido: '+seleccion)
