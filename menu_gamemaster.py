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
from Razas.razas import razas
#

def pausarYvolver():
    print('1.- Volver: ')
    while(True):
        opcion = input('# ')
        if opcion == '1':
            return
        else:
            print('Valor Ingresado no Valido')

def menuInterno1(variante):
    print('>> Menu ' + variante + ' >>')
    print('1.- Ver Todos')
    print('2.- Buscar')
    print('3.- Volver')
    opcion = input('#: ')
    return opcion

def menuInterno2(plural, singular):
    print('>> Menu ' + plural + ' >>')
    print('1.- Mostrar '+ plural)
    print('2.- Crear ' + singular)
    print('3.- Buscar ' + singular)
    print('4.- Editar '+ singular)
    print('5.- Borrar ' + singular)
    print('6.- Volver' )
    opcion = input('#: ')
    return opcion

def verificarNumero(valor):
    pass

# Menu ---------------------------------------->>
class menu_gamemaster():
    def __init__(self, enFuncionamiento, nombre, id_gameMaster):
        while(enFuncionamiento):
            os.system('cls')
            print('>> Bienvenido GameMaster: ' + nombre + ' >>')
            print('Seleccione que opcion desea ingresando el numero correspondiente a esta:')
            print('1.- Personajes')
            print('2.- Razas')
            print('3.- Poderes')
            print('4.- Habilidades')
            print('5.- Equipos')
            print('6.- Salir')
            print('>> Menu >>')
            seleccion = input('#: ')
            os.system('cls')
            # >>
            if seleccion == '1': # Personajes
                while(True):
                    opcion = menuInterno1('Personajes')
                    if opcion == '1':
                        personajesDao.mostrarPersonajesGamemaster()
                    elif opcion == '2':
                        volver = True
                        while(volver):
                            try:
                                print('Seleccione el personaje que desea ver: ')
                                personajesDao.obtenerLista()
                                personaje = int(input('#: '))
                                personajesDao.obtenerPersonajePorID(personaje)
                            except:
                                print('Valor Ingresado no Valido: ' + personaje)
                                return
                            while(True):
                                print('Que desea hacer con el personaje seleccionado: ')
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
            # >>
            elif seleccion == '2':
                while(True):
                    opcion = menuInterno2('Razas','Raza')
                    if opcion == '1': # >> Mostrar
                        razasDao.mostrar()
                    elif opcion == '2': # >> Crear
                        print('>> Crear Raza >>')
                        print('Paso 1: Ingrese el nombre de su raza')
                        nombre_raza = input('#: ')
                        print('Paso 2: Ingrese el Detalle de su Raza, que la caracteriza.')
                        detalle = input('#: ')
                        print('Paso 3: Ingrese los atributos de su raza. Se recomienda que la suma de estos no sea superior a 6')
                        destreza = input('Destreza: ')
                        fuerza = input('Fuerza: ')
                        resistencia = input('Resistencia: ')
                        nueva_raza = razas(razasDao.obtenerID(), nombre_raza, int(fuerza),int(destreza),int(resistencia),detalle)
                        razasDao.crear(nueva_raza)
                        print('Su raza ' + nombre_raza + 'a sido Creada con Exito!')
                    elif opcion == '3': # >> Buscar
                        print('Seleccione la raza que desea ver: ')
                        razasDao.mostrarLista()
                        ver_raza = input('#: ')
                        razasDao.mostrarPorID(ver_raza)
                    elif opcion == '4': # >> Editar
                        print('Seleccione la raza que desea editar, las razas basicas no pueden ser editadas: ')
                        razasDao.mostrarListaEdicion()
                        editar_raza = input('#: ')
                        razasDao.mostrarPorID(editar_raza)
                        print('Que desea modificar de la raza: '+ razasDao.obtenerNombre(editar_raza))
                        print('1.- Nombre')
                        print('2.- Fuerza')
                        print('3.- Destreza')
                        print('4.- Resistencia')
                        print('5.- Detalle')
                        modificar_raza = input('#: ')
                        if modificar_raza == '1':
                            pass
                        elif modificar_raza == '2':
                            pass
                        elif modificar_raza == '3':
                            pass
                        elif modificar_raza == '4':
                            pass
                        elif modificar_raza == '5':
                            pass
                        else:
                            print('Valor Ingresado no Valido: ' + modificar_raza)
                    elif opcion == '5': # >> Borrar
                        print('Seleccione que raza desea Borrar: ')
                        razasDao.mostrarLista()
                        borrar_raza = input('#: ')
                        razasDao.borrar(borrar_raza)
                    elif opcion == '6': # >> Salir
                        break
                    else:
                        print('Valor Ingresado no Valido: ' + opcion)
                pausarYvolver()
            # >>
            elif seleccion == '3':
                pausarYvolver()
            # >>
            elif seleccion == '4':
                pausarYvolver()
            # >>
            elif seleccion == '5':
                pausarYvolver()
            # >>
            elif seleccion == '6':
                print('>> Hasta Luego ' + nombre + ' >>')
                enFuncionamiento = False
            # >>
            else:
                print('Valor Ingresado no Valido: '+seleccion)
