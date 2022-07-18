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

def pausarYvolver():
    print('1.- Volver: ')
    while(True):
        opcion = input('# ')
        if opcion == '1':
            return
        else:
            print('Valor Ingresado no Valido')

def comprobarNumero(atributo):
    while(True):
        try:
            print('Ingrese el valor de ' + atributo)
            numero = int(input('#: '))
            if numero >= 0 and numero <= 10:
                return numero
            else:
                print('Valor Ingresado no Valido')
        except:
            print('Valor Ingresado no Valido, Ingrese un Numero por favor')

def crearPersonaje(id_jugador):
    os.system('cls')
    print('>> Creacion de Personaje >>')
    print('Ingrese el nombre de su Personaje: ')
    nombre_personaje = input('#: ').strip().capitalize()
    # Raza del Personaje
    while(True):
        print('Seleccione la Raza de su Personaje: ')
        listaID = razasDao.obtenerLista()
        id_raza = input('#: ')
        if id_raza in listaID:
            while(True):
                print('A continuacion posees 12 puntos a repartir entre los seis atributos del personaje: ')
                print('Fuerza, Destreza, Reistencia, Inteligencia, Sabiduria y Carisma')
                fuerza = comprobarNumero('Fuerza')
                destreza = comprobarNumero('Destreza')
                resistencia = comprobarNumero('Resistencia')
                inteligencia = comprobarNumero('Inteligencia')
                sabiduria = comprobarNumero('Sabiduria')
                carisma = comprobarNumero('Carisma')
                atributos = [fuerza, destreza, resistencia,
                             inteligencia, sabiduria, carisma]
                total_puntos = int(fuerza) + int(destreza) + int(resistencia) + int(inteligencia) + int(sabiduria) + int(carisma)
                if int(total_puntos) < 12:
                    print(
                        'No se distribuyeron correctamente los 12 puntos, por favor intentelo nuevamente')
                elif int(total_puntos) > 12:
                    print(
                        'Ha ingresado mas puntos de los debidos, por favor distribuyalos nuevamente')
                else:
                    while(True):
                        print('Seleccione su equipo inicial: ')
                        listaID = equipoDao.obtenerLista()
                        id_equipo = input('#: ')
                        if id_equipo in listaID:
                            atributos[0] += razasDao.obtenerFuerza(id_raza)
                            atributos[1] += razasDao.obtenerDestreza(id_raza)
                            atributos[2] += razasDao.obtenerResistencia(id_raza)
                            nuevo_personaje = personajes(int(personajesDao.obtenerID()), nombre_personaje, 1, 1, int(atributos[3]), int(atributos[4]), int(atributos[5]), 0, int(atributos[0]), int(atributos[1]), int(atributos[2]), int(id_jugador), int(id_equipo), int(id_raza))
                            personajesDao.crear(nuevo_personaje)
                            return
                        else:
                            print('Valor Ingresado no Valido: ' + id_equipo)
        else:
            print('Valor Ingresado no Valido: ' + id_raza)
            # Atributos del Personaje
            
    # Fin Creacion del Personaje

# Menu ---------------------------------------->>
class menu_jugador():
    def __init__(self, enFuncionamiento, nombre, id_jugador):
        while(enFuncionamiento):
            time.sleep(2)
            os.system('cls')
            print('>> Bienvenido Jugador: ' + nombre + ' >>')
            print(
                'Seleccione que opcion desea ingresando el numero correspondiente a esta:')
            print('1.- Crear Personajes')
            print('2.- Ver Mis Personajes')
            print('3.- Ver Razas')
            print('4.- Ver Poderes')
            print('5.- Ver Habilidades')
            print('6.- Ver Equipos')
            print('7.- Salir')
            print('>> Menu >>')
            seleccion = input('#: ')
            os.system('cls')
            if seleccion == '1': # Crear Personajes
                crearPersonaje(id_jugador)
                pausarYvolver()
            elif seleccion == '2': # Ver Mis Persoanjes
                personajesDao.obtenerPersonajeJugador(id_jugador)
                while(True):
                    print('Desea cambiar el Equipamiento de un Personaje: ')
                    print('1.- Si')
                    print('2.- No')
                    opcion = input('#: ')
                    if opcion == '1':
                        print('Seleccione que personaje desea editar: ')
                        personajesDao.obtenerListaPersonaje(id_jugador)
                        opcion = input('#: ')
                        personajesDao.modificarEquipo(opcion,personajesDao.obtenerEstado(opcion)) #Corregir
                    elif opcion == '2':
                        break
                    else:
                        print('Valor Ingresado no Valido: ' + opcion)
                pausarYvolver()
            elif seleccion == '3': # Ver Razas
                razasDao.mostrar()
                pausarYvolver()
            elif seleccion == '4': # Ver Poderes
                poderesDao.mostrar()
                pausarYvolver()
            elif seleccion == '5': # Ver Habilidades
                habilidadesDao.mostrar()
                pausarYvolver()
            elif seleccion == '6': # Ver Equipos
                equipoDao.mostrar()
                pausarYvolver()
            elif seleccion == '7': # Salir
                print('>> Hasta Luego ' + nombre + ' >>')
                enFuncionamiento = False
            else:
                print('Valor Ingresado no Valido: '+seleccion)
