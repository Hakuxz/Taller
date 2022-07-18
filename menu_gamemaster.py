import time
import os
from beautifultable import BeautifulTable
from Equipo.equipo import equipo
from os import system
# DAO's
from Equipo.equipoDao import equipoDao
from Estados.estadosDao import estadosDao
from Habilidades.habilidadesDao import habilidadesDao
from Personajes.personajesDao import personajesDao
from Personajes.personajes import personajes
from Poderes.poderes import poderes
from Poderes.poderesDao import poderesDao
from Razas.razasDao import razasDao
from Estados.estados import estados
from Razas.razas import razas
from Habilidades.habilidades import habilidades
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


def comprobarNumero():
    while(True):
        try:
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
                        print()
                        print('Paso 1: Ingrese el nombre de su raza')
                        nombre_raza = input('» ').strip()
                        print()
                        print('Paso 2: Ingrese el Detalle de su Raza, que la caracteriza.')
                        detalle = input('» ').strip()
                        print()
                        print('Paso 3: Ingrese los atributos de su raza. Se recomienda que la suma de estos no sea superior a 6')
                        print()
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
                            print('\033[1;3;33m'+'Seleccione la raza que desea editar, las razas basicas no pueden ser editadas: '+'\033[0;m')
                            print()
                            listaID = razasDao.obtenerListaEdicion()
                            editar_raza = input('» ').strip()
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
                                system('cls')
                                print('\033[1;3;33m'+'Ingrese el nuevo Nombre que desea otorgarle a la raza ' + razasDao.obtenerNombre(editar_raza)+'\033[0;m')
                                print()
                                nuevo_nombre = input('» ')
                                razasDao.modificarNombre(nuevo_nombre,editar_raza)
                                break
                            elif modificar_raza == '2':
                                system('cls')
                                print('\033[1;3;33m'+'Ingrese el nuevo valor de Fuerza que desea otorgarle a la raza ' + razasDao.obtenerNombre(editar_raza)+'\033[0;m')
                                print()
                                nuevo_atributo = input('» ')
                                razasDao.modificarFuerza(nuevo_atributo,editar_raza)
                                break
                            elif modificar_raza == '3':
                                system('cls')
                                print('\033[1;3;33m'+'Ingrese el nuevo valor de Destreza que desea otorgarle a la raza ' + razasDao.obtenerNombre(editar_raza)+'\033[0;m')
                                print()
                                nuevo_atributo = input('» ')
                                razasDao.modificarDestreza(nuevo_atributo,editar_raza)
                                break
                            elif modificar_raza == '4':
                                system('cls')
                                print('\033[1;3;33m''Ingrese el nuevo valor de Resistencia que desea otorgarle a la raza ' + razasDao.obtenerNombre(editar_raza)+'\033[0;m')
                                print()
                                nuevo_atributo = input('» ')
                                razasDao.modificarResistencia(nuevo_atributo,editar_raza)
                                break
                            elif modificar_raza == '5':
                                print('\033[1;3;33m''Ingrese el nuevo Detalle que desea otorgarle a la raza ' + razasDao.obtenerNombre(editar_raza)+'\033[0;m')
                                print()
                                nuevo_detalle = input('» ')
                                razasDao.modificarDetalle(nuevo_detalle,editar_raza)
                                break
                            else:
                                system('cls')
                                print('\033[1;3;31m''Valor '+ modificar_raza +' no Valido: '+'\033[0;m')
                                time.sleep(2)
                    elif opcion == '5': # >> Borrar
                        while(True):
                            system('cls')
                            print('\033[1;3;33m'+'Seleccione que raza desea Borrar: '+'\033[0;m')
                            listaID = razasDao.obtenerListaEdicion()
                            print()
                            borrar_raza = input('» ').strip()
                            if borrar_raza in listaID:
                                if borrar_raza == '0' or borrar_raza == '1' or borrar_raza == '2' or borrar_raza == '3':
                                    system('cls')
                                    print('\033[1;35m'+'Lo sentimos pero las razas basicas no son modificables'+'\033[0;m')
                                    time.sleep(2)
                                    break
                                razasDao.borrar(borrar_raza) # Buscar como no eliminar si la raza esta en uso
                                break
                            else:
                                system('cls')
                                print('\033[1;3;31m'+'Valor '+ opcion +' no Valido: '+'\033[0;m')
                                time.sleep(2)
                    elif opcion == '6': # >> Salir
                        break
                    else:
                        system('cls')
                        print('\033[1;3;31m'+'Valor '+ opcion +' no Valido: '+'\033[0;m')
                        time.sleep(2)
                pausarYvolver()
            # >>
            elif seleccion == '3': # Poderes
                opcion = menuInterno2('Poderes','Poder')
                if opcion == '1': # >> Mostrar Poderes
                    poderesDao.mostrar()
                elif opcion == '2': # >> Crear Poderes
                    while(True):
                        system('cls')
                        print('\033[1;4;37m'+'Crear Poder'+'\033[0;m')
                        print()
                        print('\033[1;3;33m'+'Ingrese el nombre del poder que desea crear: '+'\033[0;m')
                        nombre_poder = input('» ').strip().capitalize()
                        print()
                        print('\033[1;3;33m'+'Ingrese la descripcion de el nuevo Poder: '+'\033[0;m')
                        detalle_poder = input('» ').strip().capitalize()
                        print()
                        print('\033[1;3;33m'+'Seleccione la raza a la cual pertenece el Poder: '+'\033[0;m')
                        listaID = razasDao.obtenerLista()
                        raza_poder = input('» ').strip().capitalize()
                        if raza_poder in listaID:
                            nuevo_poder = poderes(poderesDao.obtenerID(),nombre_poder,detalle_poder,raza_poder)  
                            poderesDao.crear(nuevo_poder)
                            break
                        else:
                            system('cls')
                            print('\033[1;3;31m'+'Valor '+ raza_poder +' no Valido: '+'\033[0;m')
                            time.sleep(2)

                elif opcion == '3': # >> Buscar Poderes
                    while(True):
                        system('cls')
                        print('\033[1;4;37m'+'Buscar Poder'+'\033[0;m')
                        print()
                        print('\033[1;3;33m'+'Seleccione el Poder que busca: '+'\033[0;m')
                        print()
                        listaID = poderesDao.obtenerLista()
                        buscar_poder = input('» ').strip()
                        if buscar_poder in listaID:
                            poderesDao.mostrarPorID(buscar_poder)
                            break
                        else:
                            system('cls')
                            print('\033[1;3;31m'+'Valor '+ raza_poder +' no Valido: '+'\033[0;m')
                            time.sleep(2)

                elif opcion == '4': # >> Editar Poderes
                    while(True):
                        system('cls')
                        print('\033[1;4;37m'+'Editar Poder'+'\033[0;m')
                        print()
                        print('\033[1;3;33m'+'Seleccione el Poder que deseas editar: '+'\033[0;m')
                        print()
                        listaID = poderesDao.obtenerLista()
                        editar_poder = input('» ').strip()
                        if editar_poder in listaID:
                            poderesDao.mostrarPorID(editar_poder)
                        else:
                            system('cls')
                            print('\033[1;3;31m'+'Valor '+ raza_poder +' no Valido: '+'\033[0;m')
                            time.sleep(2)

                        system('cls')    
                        print('Que desea modificar de el Poder: '+ poderesDao.obtenerNombre(editar_poder))
                        print()
                        print('\033[1;33m'+'1.- '+'\033[0;m'+'Descripcion')
                        print('\033[1;33m'+'2.- '+'\033[0;m'+'Volver')
                        print()
                        opcion = input('» ').strip()

                        if opcion == '1':
                            system('cls')
                            print('\033[1;3;33m'+'Ingrese la nueva descripción que desea otorgarle: '+'\033[0;m')
                            nuevo_detalle_poder = input('» ').strip().capitalize()
                            poderesDao.modificarDetalle(nuevo_detalle_poder,editar_poder)
                        elif opcion == '2':
                            break
                        else:
                            system('cls')
                            print('\033[1;3;31m'+'Valor '+ opcion +' no Valido: ')
                            time.sleep(2)

                elif opcion == '5': # >> Borrar Poderes
                    while(True):
                        print('\033[1;3;33m'+'Seleccione el poder desea borrar: '+'\033[0;m')
                        print()
                        listaID = poderesDao.obtenerListaAcotada()
                        borrar_poder = input('» ').strip()
                        if borrar_poder in listaID:
                            if borrar_poder == '0'or borrar_poder == '1' or borrar_poder == '2' or borrar_poder == '3':
                                system('cls')
                                print('\033[1;3;33m'+'Lo sentimos pero los poderes basicos no son modificables'+'\033[0;m')
                                time.sleep(2)
                                break
                            poderesDao.borrar(borrar_poder)
                            break
                        else:
                            system('cls')
                            print('\033[1;3;31m'+'Valor '+ borrar_poder +' no Valido: '+'\033[0;m')
                            time.sleep(2)

                elif opcion == '6': # >> Salir Poderes
                    pass

                else:
                    system('cls')
                    print('\033[1;3;31m'+'Valor '+ opcion +' no Valido: '+'\033[0;m')
                    time.sleep(2)
                pausarYvolver()
            # >>
            elif seleccion == '4': # Habilidades
                opcion = menuInterno2('Habilidades','Habilidad')
                if opcion == '1': # >> Mostrar Habilidades
                    habilidadesDao.mostrar()
                elif opcion == '2': # >> Crear Habilidades
                    while(True):
                        system('cls')
                        print('\033[1;4;37m'+'Crear Habilidad'+'\033[0;m')
                        print()
                        print('\033[1;3;33m'+'Ingrese el nombre de la habilidad que desea crear: '+'\033[0;m')
                        nombre_habilidad = input('» ').strip().capitalize()
                        print()
                        print('\033[1;3;33m'+'Ingrese la descripcion de la nueva habilidad: '+'\033[0;m')
                        detalle_habilidad = input('» ').strip().capitalize()
                        print()
                        print('\033[1;3;33m'+'Seleccione la raza a la cual pertenece la habilidad: '+'\033[0;m')
                        listaID = razasDao.obtenerLista()
                        raza_habilidad = input('» ').strip().capitalize()
                        if raza_habilidad in listaID:
                            nueva_habilidad = habilidades(habilidadesDao.obtenerID(),nombre_habilidad,detalle_habilidad,raza_habilidad)  
                            habilidadesDao.crear(nueva_habilidad)
                            break
                        else:
                            system('cls')
                            print('\033[1;3;31m'+'Valor '+ raza_habilidad +' no Valido: '+'\033[0;m')
                            time.sleep(2)
                elif opcion == '3': # >> Buscar Habilidades
                    while(True):
                        system('cls')
                        print('\033[1;4;37m'+'Buscar Habilidad'+'\033[0;m')
                        print()
                        print('\033[1;3;33m'+'Seleccione la habilidad que busca: '+'\033[0;m')
                        listaID = habilidadesDao.obtenerLista()
                        buscar_habilidad = input('» ').strip()
                        if buscar_habilidad in listaID:
                            habilidadesDao.mostrarPorID(buscar_habilidad)
                            break
                        else:
                            system('cls')
                            print('\033[1;3;31m'+'Valor '+ raza_habilidad +' no Valido: '+'\033[0;m')
                            time.sleep(2)

                elif opcion == '4': # >> Editar Habilidades
                    while(True):
                        system('cls')
                        print('\033[1;4;37m'+'Editar Habilidad'+'\033[0;m')
                        print()
                        print('\033[1;3;33m'+'Seleccione la habilidad que deseas editar: '+'\033[0;m')
                        listaID = habilidadesDao.obtenerLista()
                        editar_habilidad = input('» ').strip()
                        if editar_habilidad in listaID:
                            habilidadesDao.mostrarPorID(editar_habilidad)
                        else:
                            system('cls')
                            print('\033[1;3;31m'+'Valor '+ raza_habilidad +' no Valido: '+'\033[0;m')
                            time.sleep(2)

                        print('Que desea modificar de la habilidad: '+ habilidadesDao.obtenerNombre(editar_habilidad))
                        print()
                        print('\033[1;33m'+'1.- '+'\033[0;m'+'Descripcion')
                        print('\033[1;33m'+'2.- '+'\033[0;m'+'Volver')
                        print()
                        opcion = input('» ').strip()
                        if opcion == '1':
                            system('cls')
                            print('\033[1;3;33m'+'Ingrese la nueva descripción que desea otorgarle: '+'\033[0;m')
                            nuevo_detalle_habilidad = input('» ').strip().capitalize()
                            habilidadesDao.modificarDetalle(nuevo_detalle_habilidad,editar_habilidad)
                            break
                        elif opcion == '2':
                            break
                        else:
                            system('cls')
                            print('\033[1;3;31m'+'Valor '+ opcion +' no Valido: '+'\033[0;m')
                            time.sleep(2)
                elif opcion == '5': # >> Borrar Habilidades
                    while(True):
                        system('cls')
                        print('\033[1;3;33m'+'Seleccione que habilidad desea borrar: '+'\033[0;m')
                        listaID = habilidadesDao.obtenerListaAcotada()
                        borrar_habilidad = input('» ').strip()
                        if borrar_habilidad in listaID:
                            if borrar_habilidad == '0'or borrar_habilidad == '1' or borrar_habilidad == '2' or borrar_habilidad == '3' or borrar_habilidad == '4'or borrar_habilidad == '5' or borrar_habilidad == '6' or borrar_habilidad == '7':
                                print('Lo sentimos pero las habilidades basicas no son modificables')
                                break
                            habilidadesDao.borrar(borrar_habilidad)
                            break
                        else:
                            print('Valor Ingresado no Valido: ' + borrar_habilidad)         
                elif opcion == '6': # >> Salir Habilidades
                    pass
                else:
                    system('cls')
                    print('\033[1;3;31m'+'Valor '+ opcion +' no Valido: '+'\033[0;m')
                    time.sleep(2)
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
                        system('cls')
                        print('\033[1;4;37m'+'Creacion de Equipo'+'\033[0;m')
                        print()
                        print('Seleccione el tipo de equipo que desea crear: ')
                        print()
                        print('\033[1;3;33m'+'1.- '+'\033[0;m'+'Ligera')
                        print('\033[1;3;33m'+'2.- '+'\033[0;m'+'Pesada')
                        print('\033[1;3;33m'+'3.- '+'\033[0;m'+'Defensa')
                        print('\033[1;3;33m'+'4.- '+'\033[0;m'+'Rango')
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
                            system('cls')
                            print('\033[1;3;31m'+'Valor '+ tipo_equipo +' no Valido: '+'\033[0;m')
                            time.sleep(2)
                            
                    print('\033[1;3;33m'+'Ingrese el nombre de su equipamiento: '+'\033[0;m')
                    nombre_equipo = input('» ').strip()
                    ejecucion = True
                    while(ejecucion):
                        system('cls')
                        print('\033[1;3;33m'+'Ingrese el tipo de daño que realiza su equipo: '+'\033[0;m')
                        print()
                        print('\033[1;33m'+'1.- '+'\033[0;m'+'Contundente')
                        print('\033[1;33m'+'2.- '+'\033[0;m'+'Cortante')
                        print('\033[1;33m'+'3.- '+'\033[0;m'+'Punzante')
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
                            system('cls')
                            print('\033[1;3;31m'+'Valor '+ tipo_dano +' no Valido: '+'\033[0;m')
                            time.sleep(2)
                            
                    print('\033[1;3;33m'+'Ingrese el daño que realiza su Equipo: '+'\033[0;m')
                    dano_equipo = input('» ').strip()
                    nuevo_equipo = equipo(equipoDao.obtenerID(),nombre_equipo,tipo_equipo,int(dano_equipo),tipo_dano)
                    equipoDao.crear(nuevo_equipo)
                elif opcion == '3':
                    while(True):
                        system('cls')
                        print('\033[1;3;33m'+'Seleccione que Equipo desea ver: '+'\033[0;m')
                        listaID = equipoDao.obtenerLista()
                        ver_equipo = input('» ').strip()
                        if ver_equipo in listaID:
                            equipoDao.mostrarPorID(ver_equipo)
                            break
                        else:
                            system('cls')
                            print('\033[1;3;31m'+'Valor '+ ver_equipo +' no Valido: '+'\033[0;m')
                            time.sleep(2)

                elif opcion == '4':
                    while(True):
                        system('cls')
                        print('\033[1;3;33m'+'Seleccione el Equipo que desea renombrar: S'+'\033[0;m')
                        listaID = equipoDao.obtenerLista()
                        id_equipo = input('» ')
                        if id_equipo in listaID:
                            system('cls')
                            print('Seleccione el nombre que desea otorgarle: ')
                            nuevo_nombre = input('» ')
                            equipoDao.cambiarNombre(nuevo_nombre,id_equipo)
                            break
                        else:
                            system('cls')
                            print('\033[1;3;31m'+'Valor '+ id_equipo +' no Valido: '+'\033[0;m')
                            time.sleep(2)

                elif opcion == '5': # corregir in if id
                    while(True):
                        system('cls')
                        print('\033[1;3;33m'+'Seleccione el equipo que desea borrar'+'\033[0;m')
                        listaID = equipoDao.obtenerLista()
                        borrar_equipo = input('» ').strip()
                        if borrar_equipo in listaID:
                            equipoDao.borrar(borrar_equipo)
                            break
                        else:
                            system('cls')
                            print('\033[1;3;31m'+'Valor '+ id_equipo +' no Valido: '+'\033[0;m')
                            time.sleep(2)

                elif opcion == '6':
                    break
                else:
                    system('cls')
                    print('\033[1;3;31m'+'Valor '+ opcion +' no Valido: '+'\033[0;m')
                    time.sleep(2)
                pausarYvolver()
            # >>
            elif seleccion == '6': # Salir
                print('\033[1;4;37m'+'Hasta Luego ' + nombre +'\033[0;m')
                enFuncionamiento = False
            # >>
            else:
                system('cls')
                print('\033[1;3;31m'+'Valor '+ seleccion +' no Valido: '+'\033[0;m')
                time.sleep(2)
