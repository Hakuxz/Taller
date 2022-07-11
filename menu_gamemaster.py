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
            elif seleccion == '2': # Razas
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
                        if editar_raza == '0' or editar_raza == '1' or editar_raza == '2' or editar_raza == '3':
                            print('Lo sentimos pero las razas basicas no son modificables')
                            break
                        razasDao.mostrarPorID(editar_raza)
                        print('Que desea modificar de la raza: '+ razasDao.obtenerNombre(editar_raza))
                        print('1.- Nombre')
                        print('2.- Fuerza')
                        print('3.- Destreza')
                        print('4.- Resistencia')
                        print('5.- Detalle')
                        modificar_raza = input('#: ')
                        if modificar_raza == '1':
                            print('Ingrese el nuevo Nombre que desea otorgarle a la raza ' + razasDao.obtenerNombre(editar_raza))
                            nuevo_nombre = input('#: ')
                            razasDao.modificarNombre(nuevo_nombre,editar_raza)
                        elif modificar_raza == '2':
                            print('Ingrese el nuevo valor de Fuerza que desea otorgarle a la raza ' + razasDao.obtenerNombre(editar_raza))
                            nuevo_atributo = input('#: ')
                            razasDao.modificarFuerza(nuevo_atributo,editar_raza)
                        elif modificar_raza == '3':
                            print('Ingrese el nuevo valor de Destreza que desea otorgarle a la raza ' + razasDao.obtenerNombre(editar_raza))
                            nuevo_atributo = input('#: ')
                            razasDao.modificarDestreza(nuevo_atributo,editar_raza)
                        elif modificar_raza == '4':
                            print('Ingrese el nuevo valor de Resistencia que desea otorgarle a la raza ' + razasDao.obtenerNombre(editar_raza))
                            nuevo_atributo = input('#: ')
                            razasDao.modificarResistencia(nuevo_atributo,editar_raza)
                        elif modificar_raza == '5':
                            print('Ingrese el nuevo Detalle que desea otorgarle a la raza ' + razasDao.obtenerNombre(editar_raza))
                            nuevo_detalle = input('#: ')
                            razasDao.modificarDetalle(nuevo_detalle,editar_raza)
                        else:
                            print('Valor Ingresado no Valido: ' + modificar_raza)
                    elif opcion == '5': # >> Borrar
                        print('Seleccione que raza desea Borrar: ')
                        razasDao.mostrarListaEdicion()
                        borrar_raza = input('#: ')
                        if borrar_raza == '0' or borrar_raza == '1' or borrar_raza == '2' or borrar_raza == '3':
                            print('Lo sentimos pero las razas basicas no son modificables')
                            break
                        razasDao.borrar(borrar_raza) # Buscar como no eliminar si la raza esta en uso
                    elif opcion == '6': # >> Salir
                        break
                    else:
                        print('Valor Ingresado no Valido: ' + opcion)
                pausarYvolver()
            # >>
            elif seleccion == '3': # Poderes
                pausarYvolver()
            # >>
            elif seleccion == '4': # Habilidades
                pausarYvolver()
            # >>
            elif seleccion == '5': # Equipo
                while(True):
                    print('>> Menu Equipo >>')
                    print('1.- Mostrar Equipos')
                    print('2.- Renombrar Equipo')
                    print('3.- Volver' )
                    opcion = input('#: ')
                    if opcion == '1':
                        equipoDao.mostrar()
                    elif opcion == '2':
                        print('Seleccione el Equipo que desea renombrar: ')
                        equipoDao.obtenerLista()
                        id_equipo = input('#: ')
                        print('Seleccione el nombre que desea otorgarle: ')
                        nuevo_nombre = input('#: ')
                        equipoDao.cambiarNombre(nuevo_nombre,id_equipo)
                    elif opcion == '3':
                        break
                    else:
                        print('Valor Ingresado no Valido: ' + opcion)
            # >>
            elif seleccion == '6': # Salir
                print('>> Hasta Luego ' + nombre + ' >>')
                enFuncionamiento = False
            # >>
            else:
                print('Valor Ingresado no Valido: '+seleccion)
