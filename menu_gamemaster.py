import time
import os
from beautifultable import BeautifulTable
# DAO's
from Equipo.equipoDao import equipoDao
from Estados.estadosDao import estadosDao
from Habilidades.habilidadesDao import habilidadesDao
from Personajes.personajesDao import personajesDao
from Personajes.personajes import personajes
from Poderes.poderesDao import poderesDao
from Razas.razasDao import razasDao
from Estados.estados import estados
#

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

def menuInterno(variante):
    print('>> Menu ' + variante + ' >>')
    print('1.- Ver Todos')
    print('2.- Buscar')
    print('3.- Volver')
    opcion = input('#: ')
    return opcion

# Menu ---------------------------------------->>
class menu_gamemaster():
    def __init__(self, enFuncionamiento, nombre, id_gameMaster):
        while(enFuncionamiento):
            time.sleep(2)
            os.system('cls')
            print('>> Bienvenido GameMaster: ' + nombre + ' >>')
            print('>> Menu >>')
            print('Seleccione que opcion desea ingresando el numero correspondiente a esta:')
            print('1.- Personajes')
            print('2.- Ver Personajes')
            print('3.- Razas')
            print('4.- Poderes')
            print('5.- Habilidades')
            print('6.- Equipos')
            print('7.- Salir')
            print('>> Menu >>')
            seleccion = input('#: ')
            os.system('cls')
            if seleccion == '1': # Personajes
                while(True):
                    opcion = menuInterno('Personajes')
                    if opcion == '1':
                        personaje_dao.mostrarPersonajesGamemaster()
                    elif opcion == '2':
                        volver = True
                        while(volver):
                            print('Seleccione el personaje que desea ver: ')
                            personajesDao.obtenerLista()
                            personaje = int(input('#: '))
                            if not personaje:
                                return 'Valor Ingresado no Valido: ' + personaje
                            else:
                                personaje_dao.obtenerPersonaje(personaje)
                                while(True):
                                    print('Que desea hacer con el personaje seleccionado:')
                                    print('1.- Otorgar experiencia')
                                    print('2.- Cambiar su estado')
                                    print('3.- Borrar')
                                    print('4.- Volver')
                                    opcion = input('#: ')
                                    if opcion == '1':
                                        print('Introdusca la experiencia optenida: ')
                                        exp = int(input('#: '))
                                        personajesDao.otorgarExp((personajesDao.obtenerExperiencia(personaje) + exp), personaje, personajesDao.obtenerNivel(personaje))
                                    elif opcion == '2':
                                        personajesDao.cambiarEstado(personaje)
                                    elif opcion == '3':
                                        personajesDao.borrar(personaje)
                                    elif opcion == '4':
                                        volver = False
                                        break
                                    else:
                                        print('Valor Ingresado no Valido: ' + opcion)
                    elif opcion == '3':
                        break
                    else:
                        print('Valor Ingresado no Valido: ' + opcion)
                pausarYvolver()
            elif seleccion == '2':
                pausarYvolver()
            elif seleccion == '3':
                pausarYvolver()
            elif seleccion == '4':
                pausarYvolver()
            elif seleccion == '5':
                pausarYvolver()
            elif seleccion == '6':
                pausarYvolver()
            elif seleccion == '7':
                print('>> Hasta Luego ' + nombre + ' >>')
                enFuncionamiento = False
            else:
                print('Valor Ingresado no Valido: '+seleccion)
