import time
import os
from beautifultable import BeautifulTable
from Equipo.equipo import equipo
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
        opcion = input('# ').strip()
        if opcion == '1':
            break
        else:
            print('Valor Ingresado no Valido')

def menuInterno1(variante):
    print('>> Menu ' + variante + ' >>')
    print('1.- Ver Todos')
    print('2.- Buscar')
    print('3.- Volver')
    opcion = input('#: ').strip()
    return opcion

def menuInterno2(plural, singular):
    print('>> Menu ' + plural + ' >>')
    print('1.- Mostrar '+ plural)
    print('2.- Crear ' + singular)
    print('3.- Buscar ' + singular)
    print('4.- Editar '+ singular)
    print('5.- Borrar ' + singular)
    print('6.- Volver' )
    opcion = input('#: ').strip()
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
            seleccion = input('#: ').strip()
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
                                opcion = input('#: ').strip()
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
                        nombre_raza = input('#: ').strip()
                        print('Paso 2: Ingrese el Detalle de su Raza, que la caracteriza.')
                        detalle = input('#: ').strip()
                        print('Paso 3: Ingrese los atributos de su raza. Se recomienda que la suma de estos no sea superior a 6')
                        destreza = input('Destreza: ').strip()
                        fuerza = input('Fuerza: ').strip()
                        resistencia = input('Resistencia: ').strip()
                        nueva_raza = razas(razasDao.obtenerID(), nombre_raza, int(fuerza),int(destreza),int(resistencia),detalle)
                        razasDao.crear(nueva_raza)
                        print('Su raza ' + nombre_raza + 'a sido Creada con Exito!')
                    elif opcion == '3': # >> Buscar
                        print('Seleccione la raza que desea ver: ')
                        razasDao.mostrarLista()
                        ver_raza = input('#: ').strip()
                        razasDao.mostrarPorID(ver_raza)
                    elif opcion == '4': # >> Editar
                        print('Seleccione la raza que desea editar, las razas basicas no pueden ser editadas: ')
                        razasDao.mostrarListaEdicion()
                        editar_raza = input('#: ').strip()
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
                        modificar_raza = input('#: ').strip()
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
                        borrar_raza = input('#: ').strip()
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
                opcion = menuInterno2('Equipos','Equipo')
                if opcion == '1':
                    equipoDao.mostrar()
                elif opcion == '2':
                    tipo_equipo = ''
                    nombre_equipo = ''
                    tipo_dano = ''
                    dano_equipo = 0
                    ejecucion = True
                    while(ejecucion):
                        print('>> Creacion de Equipo >>')
                        print('Seleccione el tipo de equipo que desea crear: ')
                        print('1.- Ligera')
                        print('2.- Pesada')
                        print('3.- Defensa')
                        print('4.- Rango')
                        tipo_equipo = input('#: ').strip()
                        if tipo_equipo == '1':
                            tipo_equipo = 'Ligero'
                            ejecucion = False
                        elif tipo_equipo == '2':
                            tipo_equipo = 'Pesado'
                            ejecucion = False
                        elif tipo_equipo == '3':
                            tipo_equipo = 'Defensa'
                            ejecucion = False
                        elif tipo_equipo == '4':
                            tipo_equipo = 'Rango'
                            ejecucion = False
                        else:
                            print('Valor Ingresado no Valido: ' + tipo_equipo)
                    print('Ingrese el nombre de su equipamiento: ')
                    nombre_equipo = input('#: ').strip()
                    ejecucion = True
                    while(ejecucion):
                        print('Ingrese el tipo de daño que realiza su equipo: ')
                        print('1.- Contundente')
                        print('2.- Cortante')
                        print('3.- Punzante')
                        tipo_dano = input('#: ').strip()
                        if tipo_dano == '1':
                            tipo_dano = 'Contundente'
                            ejecucion = False
                        elif tipo_dano == '2':
                            tipo_dano = 'Cortante'
                            ejecucion = False
                        elif tipo_dano == '3':
                            tipo_dano = 'Punzante'
                            ejecucion = False
                        else:
                            print('Valor Ingresado no Valido: ' + tipo_dano)
                    print('Ingrese el daño que realiza su Equipo: ')
                    dano_equipo = input('#: ').strip()
                    nuevo_equipo = equipo(equipoDao.obtenerID(),nombre_equipo,tipo_equipo,int(dano_equipo),tipo_dano)
                    equipoDao.crear(nuevo_equipo)
                elif opcion == '3':
                    print('Seleccione que Equipo desea ver: ')
                    equipoDao.obtenerLista()
                    ver_equipo = input('#: ').strip()
                    equipoDao.mostrarPorID(ver_equipo)
                elif opcion == '4':
                    print('>> Seleccione el Equipo que desea renombrar: S')
                    equipoDao.obtenerLista()
                    id_equipo = input('#: ')
                    print('Seleccione el nombre que desea otorgarle: ')
                    nuevo_nombre = input('#: ')
                    equipoDao.cambiarNombre(nuevo_nombre,id_equipo)
                elif opcion == '5':
                    print('Seleccione el equipo que desea borrar')
                    equipoDao.obtenerLista()
                    borrar_equipo = input('#: ').strip()
                    equipoDao.borrar(borrar_equipo)
                elif opcion == '6':
                    break
                else:
                    print('Valor Ingresado no Valido: ' + opcion)
                pausarYvolver()
            # >>
            elif seleccion == '6': # Salir
                print('>> Hasta Luego ' + nombre + ' >>')
                enFuncionamiento = False
            # >>
            else:
                print('Valor Ingresado no Valido: '+seleccion)
