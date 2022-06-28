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
    print('1.- Ver ')
    print('2.- Buscar')
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
                opcion = menuInterno('Personajes')
                if opcion == '1':
                    personaje_dao.mostrarPersonajesGamemaster()
                elif opcion == '2':
                    while(True):
                        print('Seleccione el personaje que desea ver: ')
                        personajesDao.obtenerLista()
                        personaje = input('#: ')
                        if not personaje:
                            return 'Valor Ingresado no Valido: ' + personaje
                        else:
                            personaje_dao.obtenerPersonaje(personaje)
                        break
                else:
                    print('Valor Ingresado no Valido: ' + personaje)
                    break
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
