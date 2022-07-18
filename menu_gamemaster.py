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
from os import system
#


def pausarYvolver():
    print('\033[1;33m'+'1.- '+'Volver: '+'\033[0;m')
    while(True):
        opcion = input('» ').strip()
        if opcion == '1':
            break
        else:
            print('\033[1;3;31m'+'Valor '+ opcion +' no Valido'+'\033[0;m')


def menuInterno1(variante):
    print('\033[1;37m'+'Menu '+'\033[0;m' + variante +'\033[0;m')
    print()
    print('\033[1;33m'+'1.- '+'\033[0;m'+'Ver Todos'+'\033[0;m')
    print('\033[1;33m'+'2.- '+'\033[0;m'+'Buscar'+'\033[0;m')
    print('\033[1;33m'+'3.- '+'\033[0;m'+'Volver'+'\033[0;m')
    print()
    opcion = input('» ').strip()
    return opcion


def menuInterno2(plural, singular):
    print('\033[1;37m'+'Menu '+'\033[0;m' + plural+'\033[0;m')
    print()
    print('\033[1;33m'+'1.- '+'\033[0;m'+'Mostrar ' + plural+'\033[0;m')
    print('\033[1;33m'+'2.- '+'\033[0;m'+'Crear ' + singular+'\033[0;m')
    print('\033[1;33m'+'3.- '+'\033[0;m'+'Buscar ' + singular+'\033[0;m')
    print('\033[1;33m'+'4.- '+'\033[0;m'+'Editar ' + singular+'\033[0;m')
    print('\033[1;33m'+'5.- '+'\033[0;m'+'Borrar ' + singular+'\033[0;m')
    print('\033[1;33m'+'6.- '+'\033[0;m'+'Volver'+'\033[0;m')
    print()
    opcion = input('» ').strip()
    return opcion


def verificarEntero(atributo, valor):
    pass

# Menu ---------------------------------------->>
class menu_gamemaster():
    def __init__(self, enFuncionamiento, nombre, id_gameMaster):
        while(enFuncionamiento):
            os.system('cls')
            print('\033[4;37m'+'Bienvenido: '+'\033[0;m'+ nombre +'\033[0;m')
            print()
            print('\033[1;3;33m'+'Seleccione que opcion desea ingresando el numero correspondiente a esta:'+'\033[0;m')
            time.sleep(4)
            os.system('cls')
            print('\033[1;33m'+'1.- '+'\033[0;m'+'Personajes'+'\033[0;m')
            print('\033[1;33m'+'2.- '+'\033[0;m'+'Razas'+'\033[0;m')
            print('\033[1;33m'+'3.- '+'\033[0;m'+'Poderes'+'\033[0;m')
            print('\033[1;33m'+'4.- '+'\033[0;m'+'Habilidades'+'\033[0;m')
            print('\033[1;33m'+'5.- '+'\033[0;m'+'Equipos'+'\033[0;m')
            print('\033[1;33m'+'6.- '+'\033[0;m'+'Salir'+'\033[0;m')
            print()
            seleccion = input('Opción: ').strip()
            os.system('cls')
            # >>
            if seleccion == '1':  # Personajes
                while(True):
                    opcion = menuInterno1('\033[1;33m'+'Personajes'+'\033[0;m')
                    if opcion == '1':
                        personajesDao.mostrarPersonajesGamemaster()
                    elif opcion == '2':
                        volver = True
                        while(volver):
                                print('\033[1;33m'+'Seleccione el personaje que desea ver: '+'\033[0;m')
                                listaID = personajesDao.obtenerLista()
                                personaje = int(input('» '))
                                if personaje in listaID:
                                    personajesDao.obtenerPersonajePorID(personaje)
                                    volver = False
                                else:
                                    print('\033[1;3;31m'+'Valor '+ personaje +' no Valido: '+'\033[0;m')
                        volver = True
                        while(volver):
                                system('cls')
                                print('\033[1;3;33m'+'Que desea hacer con el personaje seleccionado: '+'\033[0;m')
                                print('\033[1;33m'+'1.-'+'\033[0;m'+'Otorgar experiencia')
                                print('\033[1;33m'+'2.-'+'\033[0;m'+'Cambiar su estado')
                                print('\033[1;33m'+'3.-'+'\033[0;m'+'Borrar')
                                print('\033[1;33m'+'4.-'+'\033[0;m'+'Volver')
                                opcion = input('» ').strip()
                                if opcion == '1':
                                    print('\033[1;3;33m'+'Introdusca la experiencia optenida: '+'\033[0;m')
                                    exp = int(input('» '))
                                    personajesDao.otorgarExp((personajesDao.obtenerExperiencia(personaje) + exp), personaje, personajesDao.obtenerNivel(personaje))
                                elif opcion == '2':
                                    personajesDao.cambiarEstado(personaje)
                                elif opcion == '3':
                                    personajesDao.borrar(personaje)
                                elif opcion == '4':
                                    volver = False
                                    break
                                else:
                                    print('\033[1;3;31m'+'Valor '+opcion+' no Valido: '+'\033[0;m')
                    elif opcion == '3':
                        break
                    else:
                        print('\033[1;3;m'+'Valor '+opcion+' no Valido: '+'\033[0;m')
            # >>
            elif seleccion == '2': # Razas
                while(True):
                    opcion = menuInterno2('Razas','Raza')
                    if opcion == '1': # >> Mostrar
                        razasDao.mostrar()
                    elif opcion == '2': # >> Crear
                        print('\033[4;37m'+'Crear Raza'+'\033[0;m')
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
                        print('\033[1;3;32m'+'Su raza ' + nombre_raza + 'a sido Creada con Exito!'+'\033[0;m')
                    elif opcion == '3': # >> Buscar
                        while(True):
                            print('\033[1+3;33m'+'Seleccione la raza que desea ver: '+'\033[0;m')
                            listaID = razasDao.obtenerLista()
                            ver_raza = input('» ').strip()
                            if ver_raza in listaID:
                                razasDao.mostrarPorID(ver_raza)
                                break
                            else:
                                print('\033[1;3;31m'+'Valor '+ver_raza+' no Valido: '+'\033[0;m')
                    elif opcion == '4': # >> Editar
                        while(True):
                            system('cls')
                            print('\033[0;m'+'Seleccione la raza que desea editar, las razas basicas no pueden ser editadas: '+'\033[0;m')
                            listaID = razasDao.obtenerListaEdicion()
                            editar_raza = input('#: ').strip()
                            if editar_raza in listaID:
                                if editar_raza == '0' or editar_raza == '1' or editar_raza == '2' or editar_raza == '3':
                                    print('\033[1;3;31m'+'Lo sentimos pero las razas basicas no son modificables'+'\033[0;m')
                                    break
                                razasDao.mostrarPorID(editar_raza)
                            else:
                                print('\033[1;3;31m'+'Valor '+ opcion +' no Valido: '+'\033[0;m')
                            print('\033[1;3;33m'+'Que desea modificar de la raza: '+ razasDao.obtenerNombre(editar_raza)+'\033[0;m')
                            print('\033[1;33m'+'1.- '+'\033[0;m'+'Nombre'+'\033[0;m') 
                            print('\033[1;33m'+'2.- '+'\033[0;m'+'Fuerza'+'\033[0;m')
                            print('\033[1;33m'+'3.- '+'\033[0;m'+'Destreza'+'\033[0;m')
                            print('\033[1;33m'+'4.- '+'\033[0;m'+'Resistencia'+'\033[0;m')
                            print('\033[1;33m'+'5.- '+'\033[0;m'+'Detalle'+'\033[0;m')
                            print()
                            modificar_raza = input('» ').strip()
                            if modificar_raza == '1':
                                print('\033[1;3;33m'+'Ingrese el nuevo Nombre que desea otorgarle a la raza ' + razasDao.obtenerNombre(editar_raza)+'\033[0;m')
                                nuevo_nombre = input('» ')
                                razasDao.modificarNombre(nuevo_nombre,editar_raza)
                                break
                            elif modificar_raza == '2':
                                print('\033[1;3;33m'+'Ingrese el nuevo valor de Fuerza que desea otorgarle a la raza ' + razasDao.obtenerNombre(editar_raza)+'\033[0;m')
                                nuevo_atributo = input('» ')
                                razasDao.modificarFuerza(nuevo_atributo,editar_raza)
                                break
                            elif modificar_raza == '3':
                                print('\033[1;3;33m'+'Ingrese el nuevo valor de Destreza que desea otorgarle a la raza ' + razasDao.obtenerNombre(editar_raza)+'\033[0;m')
                                nuevo_atributo = input('» ')
                                razasDao.modificarDestreza(nuevo_atributo,editar_raza)
                                break
                            elif modificar_raza == '4':
                                print('\033[1;3;33m''Ingrese el nuevo valor de Resistencia que desea otorgarle a la raza ' + razasDao.obtenerNombre(editar_raza)+'\033[0;m')
                                nuevo_atributo = input('» ')
                                razasDao.modificarResistencia(nuevo_atributo,editar_raza)
                                break
                            elif modificar_raza == '5':
                                print('\033[1;3;33m''Ingrese el nuevo Detalle que desea otorgarle a la raza ' + razasDao.obtenerNombre(editar_raza)+'\033[0;m')
                                nuevo_detalle = input('» ')
                                razasDao.modificarDetalle(nuevo_detalle,editar_raza)
                                break
                            else:
                                print('\033[1;3;31m''Valor '+ modificar_raza +' no Valido: '+'\033[0;m')
                    elif opcion == '5': # >> Borrar
                        while(True):
                            print('\033[1;3;33m'+'Seleccione que raza desea Borrar: '+'\033[0;m')
                            listaID = razasDao.obtenerListaEdicion()
                            borrar_raza = input('» ').strip()
                            if borrar_raza in listaID:
                                if borrar_raza == '0' or borrar_raza == '1' or borrar_raza == '2' or borrar_raza == '3':
                                    print('\033[1;35m'+'Lo sentimos pero las razas basicas no son modificables'+'\033[0;m')
                                    break
                                razasDao.borrar(borrar_raza) # Buscar como no eliminar si la raza esta en uso
                                break
                            else:
                                print('\033[1;3;31m'+'Valor '+ opcion +' no Valido: '+'\033[0;m')
                    elif opcion == '6': # >> Salir
                        break
                    else:
                        print('\033[1;3;31m'+'Valor '+ opcion +' no Valido: '+'\033[0;m')
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
                        print('\033[1;4;37m'+'Creacion de Equipo'+'\033[0;m')
                        print()
                        print('\033[1;3;33m'+'Seleccione el tipo de equipo que desea crear: '+'\033[0;m')
                        time.sleep(4)
                        system('cls')
                        print('\033[1;33m'+'1.- '+'\033[0;m'+'Ligera'+'\033[0;m')
                        print('\033[1;33m'+'2.- '+'\033[0;m'+'Pesada'+'\033[0;m')
                        print('\033[1;33m'+'3.- '+'\033[0;m'+'Defensa'+'\033[0;m')
                        print('\033[1;33m'+'4.- '+'\033[0;m'+'Rango'+'\033[0;m')
                        print()
                        tipo_equipo = input('» ').strip()
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
                            print('\033[1;3;31m'+'Valor '+ tipo_equipo +' no Valido: '+'\033[0;m')
                    print('Ingrese el nombre de su equipamiento: ')
                    nombre_equipo = input('#: ').strip()
                    ejecucion = True
                    while(ejecucion):
                        print('\033[1;3;33m'+'Ingrese el tipo de daño que realiza su equipo: '+'\033[0;m')
                        print()
                        print('\033[1;33m'+'1.- '+'\033[0;m'+'Contundente'+'\033[0;m')
                        print('\033[1;33m'+'2.- '+'\033[0;m'+'Cortante'+'\033[0;m')
                        print('\033[1;33m'+'3.- '+'\033[0;m'+'Punzante'+'\033[0;m')
                        print()
                        tipo_dano = input('» ').strip()
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
                            print('\033[1;3;31m'+'Valor '+ tipo_dano +' no Valido: '+'\033[0;m')
                            
                    print('\033[1;3;33m'+'Ingrese el daño que realiza su Equipo: '+'\033[0;m')
                    dano_equipo = input('» ').strip()
                    nuevo_equipo = equipo(equipoDao.obtenerID(),nombre_equipo,tipo_equipo,int(dano_equipo),tipo_dano)
                    equipoDao.crear(nuevo_equipo)
                elif opcion == '3':
                    while(True):
                        print('\033[1;3;33m'+'Seleccione que Equipo desea ver: '+'\033[0;m')
                        listaID = equipoDao.obtenerLista()
                        ver_equipo = input('» ').strip()
                        if ver_equipo in listaID:
                            equipoDao.mostrarPorID(ver_equipo)
                            break
                        else:
                            print('\033[1;3;31m'+'Valor '+ ver_equipo +' no Valido: '+'\033[0;m')
                elif opcion == '4':
                    while(True):
                        print('\033[1;3;33m'+'Seleccione el Equipo que desea renombrar: S'+'\033[0;m')
                        listaID = equipoDao.obtenerLista()
                        id_equipo = input('» ')
                        if id_equipo in listaID:
                            print('\033[1;3;33m'+'Seleccione el nombre que desea otorgarle: '+'\033[0;m')
                            nuevo_nombre = input('» ')
                            equipoDao.cambiarNombre(nuevo_nombre,id_equipo)
                            break
                        else:
                            print('\033[1;3;33m'+'Valor '+ id_equipo +' no Valido: '+'\033[0;m')
                elif opcion == '5': # corregir in if id
                    while(True):
                        print('\033[1;3;33m'+'Seleccione el equipo que desea borrar'+'\033[0;m')
                        listaID = equipoDao.obtenerLista()
                        borrar_equipo = input('» ').strip()
                        if borrar_equipo in listaID:
                            equipoDao.borrar(borrar_equipo)
                            break
                        else:
                            print('\033[1;3;31m'+'Valor '+ id_equipo +' no Valido: '+'\033[0;m')
                elif opcion == '6':
                    break
                else:
                    print('\033[1;3;31m'+'Valor '+ opcion +' no Valido: '+'\033[0;m')
                pausarYvolver()
            # >>
            elif seleccion == '6': # Salir
                system('cls')
                print('\033[1;37m'+'Hasta Luego ' + nombre+'\033[0;m')
                enFuncionamiento = False
                time.sleep(1)
            # >>
            else:
                print('\033[1;3;31m'+'Valor '+ seleccion +' no Valido: '+'\033[0;m')
