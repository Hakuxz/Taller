import time
import os
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


# Menu ---------------------------------------->>
class menu_gamemaster():
    def __init__(self, enFuncionamiento, nombre, id_gameMaster):
        while(enFuncionamiento):
            time.sleep(2)
            os.system('cls')
            print('>> Bienvenido GameMaster: ' + nombre + ' >>')
            print('>> Menu >>')
            print(
                'Seleccione que opcion desea ingresando el numero correspondiente a esta:')
            print('1.- Crear Personajes')
            print('2.- Ver Mis Personajes')
            print('3.- Razas')
            print('4.- Poderes')
            print('5.- Habilidades')
            print('6.- Equipos')
            print('7.- Salir')
            print('>> Menu >>')
            seleccion = input('#: ')
            os.system('cls')
            if seleccion == '1':
                pass
            elif seleccion == '2':
                pass
            elif seleccion == '3':
                pass
            elif seleccion == '4':
                pass
            elif seleccion == '5':
                pass
            elif seleccion == '6':
                pass
            elif seleccion == '7':
                print('>> Hasta Luego ' + nombre + ' >>')
                enFuncionamiento = False
            else:
                print('Valor Ingresado no Valido: '+seleccion)
