import time
import os
from os import system
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


def pausarYvolver():
    system('cls')
    print('1.- Volver: ')
    while(True):
        opcion = input('» ')
        if opcion == '1':
            return
        else:
            system('cls')
            print('\033[1;3;31m'+'Valor Ingresado no Valido'+'\033[0;m')
            time.sleep(2)

def comprobarNumero(atributo):
    while(True):
        try:
            print('\033[1;3;33m'+'Ingrese el valor de ' + atributo+'\033[0;m')
            numero = int(input('» '))
            if numero >= 0 and numero <= 10:
                return numero
            else:
                system('cls')
                print('\033[1;3;31m'+'Valor Ingresado no Valido'+'\033[0;m')
                time.sleep(2)
        except:
            system('cls')
            print('\033[1;3;31m'+'Valor Ingresado no Valido, Ingrese un Numero por favor'+'\033[0;m')
            time.sleep(2)


def crearPersonaje(id_jugador):
    system('cls')
    print('\033[1;4;37m'+'Creacion de Personaje'+'\033[0;m')
    print()
    print('\033[1;3;33m''Ingrese el nombre de su Personaje: '+'\033[0;m')
    print()
    nombre_personaje = input('» ').capitalize().strip()
    # Raza del Personaje
    while(True):
        print('\033[1;3;33m'+'Seleccione la Raza de su Personaje: '+'\033[0;m')
        listaID = razasDao.obtenerLista()
        print()
        id_raza = input('» ')
        if id_raza in listaID:
            while(True):
                print(
                    'A continuacion posees 12 puntos a repartir entre los seis atributos del personaje: ')
                print('Fuerza, Destreza, Reistencia, Inteligencia, Sabiduria y Carisma')
                print()
                fuerza = comprobarNumero('Fuerza')
                destreza = comprobarNumero('Destreza')
                resistencia = comprobarNumero('Resistencia')
                inteligencia = comprobarNumero('Inteligencia')
                sabiduria = comprobarNumero('Sabiduria')
                carisma = comprobarNumero('Carisma')
                atributos = [fuerza, destreza, resistencia,
                             inteligencia, sabiduria, carisma]
                total_puntos = int(fuerza) + int(destreza) + int(resistencia) + \
                    int(inteligencia) + int(sabiduria) + int(carisma)
                if int(total_puntos) < 12:
                    print(
                        '\033[3;31m'+'No se distribuyeron correctamente los 12 puntos, por favor intentelo nuevamente'+'\033[0;m')
                elif int(total_puntos) > 12:
                    print(
                        '\033[3;31m'+'Ha ingresado mas puntos de los debidos, por favor distribuyalos nuevamente'+'\033[0;m')
                else:
                    while(True):
                        system('cls')
                        print('Seleccione su equipo inicial: ')
                        listaID = equipoDao.obtenerLista()
                        print()
                        id_equipo = input('» ')
                        if id_equipo in listaID:
                            atributos[0] += razasDao.obtenerFuerza(id_raza)
                            atributos[1] += razasDao.obtenerDestreza(id_raza)
                            atributos[2] += razasDao.obtenerResistencia(
                                id_raza)
                            nuevo_personaje = personajes(int(personajesDao.obtenerID()), nombre_personaje, 1, 1, int(atributos[3]), int(atributos[4]), int(
                                atributos[5]), 0, int(atributos[0]), int(atributos[1]), int(atributos[2]), int(id_jugador), int(id_equipo), int(id_raza))
                            personajesDao.crear(nuevo_personaje)
                            return
                        else:
                            os.system('cls')
                            print(chr(27)+"[1;31m"+'El Valor ' + id_equipo + ' no es Valido!')
                            time.sleep(1)
        else:
            os.system('cls')
            print(chr(27)+"[1;31m"+'El Valor ' + id_raza + ' no es Valido!')
            time.sleep(1)
            # Atributos del Personaje

    # Fin Creacion del Personaje

# Menu ---------------------------------------->>


class menu_jugador():
    def __init__(self, enFuncionamiento, nombre, id_jugador):
        while(enFuncionamiento):
            system('cls')
            print('\033[1;4;37m'+'Bienvenido: ' + nombre+'\033[0;m')
            print()
            print('\033[1;3;33m'+
                'Seleccione que opcion desea ingresando el numero correspondiente a esta:'+'\033[0;m') 
            time.sleep(4)
            system('cls')
            print(chr(27)+"[1;33m"+'1.- ' + chr(27) +
                  "[0;37m"+'Crear Personajes')
            print(chr(27)+"[1;33m"+'2.- ' + chr(27) +
                  "[0;37m"+'Ver Mis Personajes')
            print(chr(27)+"[1;33m"+'3.- ' + chr(27)+"[0;37m"+'Ver Razas')
            print(chr(27)+"[1;33m"+'4.- ' + chr(27)+"[0;37m"+'Ver Poderes')
            print(chr(27)+"[1;33m"+'5.- ' + chr(27)+"[0;37m"+'Ver Habilidades')
            print(chr(27)+"[1;33m"+'6.- ' + chr(27)+"[0;37m"+'Ver Equipos')
            print(chr(27)+"[1;33m"+'0.- ' + chr(27)+"[0;37m"+'Salir')
            print()
            seleccion = input('Opción: ')
            system('cls')
            if seleccion == '1':  # Crear Personajes
                crearPersonaje(id_jugador)
                pausarYvolver()
            elif seleccion == '2':  # Ver Mis Persoanjes
                personajesDao.obtenerPersonajeJugador(id_jugador)
                while(True):
                    print('\033[1;3;33m'+'Desea cambiar el Equipamiento de un Personaje: '+'\033[0;m')
                    print()
                    print(chr(27)+"[1;33m"+'1.- ' + chr(27)+"[0;37m"+'Si')
                    print(chr(27)+"[1;33m"+'2.- ' + chr(27)+"[0;37m"+'No')
                    print()
                    opcion = input('Opción: ')
                    if opcion == '1':
                        print('\033[1;3;33m'+'Seleccione que personaje desea editar: '+'\033[0;m')
                        personajesDao.obtenerListaPersonaje(id_jugador)
                        opcion = input('» ')
                        personajesDao.modificarEquipo(
                            opcion, personajesDao.obtenerEstado(opcion))  # Corregir
                    elif opcion == '2':
                        break
                    else:
                        print(+'\033[1;3;31m'+'Opción '+ opcion +' no Valida!'+'\033[0;m')
                pausarYvolver()
            elif seleccion == '3':  # Ver Razas
                razasDao.mostrar()
                pausarYvolver()
            elif seleccion == '4':  # Ver Poderes
                poderesDao.mostrar()
                pausarYvolver()
            elif seleccion == '5':  # Ver Habilidades
                habilidadesDao.mostrar()
                pausarYvolver()
            elif seleccion == '6':  # Ver Equipos
                equipoDao.mostrar()
                pausarYvolver()
            elif seleccion == '0':  # Salir
                print('\033[1;37m'+'Hasta Luego '+ nombre + '\033[0;m')
                enFuncionamiento = False
            else:
                os.system('cls')
                print(chr(27)+"[1;3;31m"+'La Opción ' +
                      seleccion + ' Ingresada no es Valida!')
                time.sleep(1)
