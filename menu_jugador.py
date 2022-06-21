import time
import os
#DAOs
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

# Menu ---------------------------------------->>
class menu_jugador():
    def __init__(self,enFuncionamiento,nombre):
        # imports Dao's
        equipo_dao = equipoDao()
        habilidad_dao = habilidadesDao()
        personaje_dao = habilidadesDao()
        poder_dao = poderesDao()
        raza_dao = razasDao()
        #
        while(enFuncionamiento):
            time.sleep(2)
            os.system('cls')
            print('<< Bienvenido Jugador: ' + nombre + ' >>')
            print('<<------------------------------<< Menu >>------------------------------>>')
            print('Seleccione que opcion desea ingresando el numero corrrespondiente a esta:')
            print('1.- Crear Personajes')
            print('2.- Personajes')
            print('3.- Razas')
            print('4.- Poderes')
            print('5.- Habilidades')
            print('6.- Equipos')
            print('7.- Salir')
            print('<<------------------------------<< Menu >>------------------------------>>')
            seleccion = input('#: ')
            os.system('cls')
            if seleccion == '1':
                pass
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