import time
import os
# DAO's
from Equipo.equipoDao import equipoDao
from Estados.estadosDao import estadosDao
from Habilidades.habilidadesDao import habilidadesDao
from Personajes.personajesDao import personajesDao
from Poderes.poderesDao import poderesDao
from Razas.razasDao import razasDao
from Estados.estados import estados
#
from Personajes.personajes import personajes

# imports Dao's
equipo_dao = equipoDao()
habilidad_dao = habilidadesDao()
personaje_dao = personajesDao()
poder_dao = poderesDao()
raza_dao = razasDao()
estados_dao = estadosDao()
#


def pausarYvolver():
    print('1.- Volver: ')
    while(True):
        opcion = input('# ')
        if opcion == '1':
            return
        else:
            print('Valor Ingresado no Valido')


def crearPersonaje(id_jugador):
    os.system('cls')
    print('>> Creacion de Personaje >>')
    print('Ingrese el nombre de su Personaje: ')
    nombre_personaje = input('#: ')
    # Raza del Personaje
    while(True):
        print('Seleccione la Raza de su Personaje: ')
        raza_dao.obtenerLista()
        id_raza = input('#: ')
        tipo_raza = raza_dao.buscarID(id_raza)
        if not tipo_raza:
            print('Valor Ingresado no Valido: ' + id_raza)
        else:
            # Atributos del Personaje
            while(True):
                print(
                    'A continuacion posees 12 puntos a repartir entre los seis atributos del personaje: Fuerza, Destreza, Reistencia, Inteligencia, Sabiduria y Carisma'
                )
                fuerza = int(input('Fuerza: #: '))
                destreza = int(input('Destreza: #: '))
                resistencia = int(input('Resistencia: #: '))
                inteligencia = int(input('Inteligencia: #: '))
                sabiduria = int(input('Sabiduria: #: '))
                carisma = int(input('Carisma: #: '))
                atributos = [fuerza, destreza, resistencia,
                             inteligencia, sabiduria, carisma]
                total_puntos = int(fuerza) + int(destreza) + int(resistencia) + \
                    int(inteligencia) + int(sabiduria) + int(carisma)
                if int(total_puntos) < 12:
                    print(
                        'No se distribuyeron correctamente los 12 puntos, por favor intentelo nuevamente')
                elif int(total_puntos) > 12:
                    print(
                        'Ha ingresado mas puntos de los debidos, por favor distribuyalos nuevamente')
                else:
                    atributos[0] += raza_dao.buscarFuerza(id_raza)
                    atributos[1] += raza_dao.buscarDestreza(id_raza)
                    atributos[2] += raza_dao.buscarResistencia(id_raza)
                    nuevo_personaje = personajes(personaje_dao.buscarID(), nombre_personaje, 1, 1, int(atributos[3]), int(atributos[4]), int(atributos[5]), 0, int(atributos[0]), int(atributos[1]), int(atributos[2]), int(id_jugador), 0, int(id_raza))
                    personaje_dao.crear(nuevo_personaje)
                    return
    # Fin Creacion del Personaje

# Menu ---------------------------------------->>
class menu_jugador():
    def __init__(self, enFuncionamiento, nombre, id_jugador):
        while(enFuncionamiento):
            time.sleep(2)
            os.system('cls')
            print(id_jugador)
            print('>> Bienvenido Jugador: ' + nombre + ' >>')
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
                crearPersonaje(id_jugador)
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
                print('>> Hasta Luego ' + nombre)
                enFuncionamiento = False
            else:
                print('Valor Ingresado no Valido: '+seleccion)
