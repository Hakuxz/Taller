from os import  system
import time
from coneccion import coneccion
from t_jugador import t_jugador
from t_jugadorDAO import t_jugadorDAO
from t_gamemaster import t_gamemaster
from t_gamemasterDAO import t_gamemasterDAO
from menu_jugador import menu_jugador
from menu_gamemaster import menu_gamemaster

coneccion.getStartConnection()
jugador_dao = t_jugadorDAO()
gamemaster_dao = t_gamemasterDAO()

enFunconamiento = True


def ingresoUsuario():
    system('cls')
    print(chr(27)+"[1;4;37m"+'Iniciar Sesión'+'\033[0;m')
    print()
    print(chr(27)+"[1;3;33m"+'Ingrese su Nombre de Usuario: ')
    print()
    nnUsuario = input("\033[0;m"+'» ').upper().strip()  # Ingreso Nickname en Mayuscula
    print()
    print(chr(27)+"[1;3;33m"+'Ingrese su Contraseña: ')
    print()
    ccUsuario = input("\033[0;m"+'» ').strip()
    if jugador_dao.comprobarUsuario(nnUsuario, ccUsuario):
        menu = menu_jugador(enFunconamiento, nnUsuario,
                            jugador_dao.obtenerID(nnUsuario))
    elif gamemaster_dao.comprobarUsuario(nnUsuario, ccUsuario):
        menu = menu_gamemaster(enFunconamiento, nnUsuario,
                               jugador_dao.obtenerID(nnUsuario))
    else:
        system('cls')
        print(chr(27)+"[1;31m"+'Su Nombre o Contraseña no son validos!')
        time.sleep(1)


def crearUsuario():  # Paso 1
    system('cls')
    print(chr(27)+"[1;4;37m"+'Creacion de Usuario'+'\033[0;m')
    print('')
    print(chr(27)+"[1;33m"+'1.- '+ chr(27)+"[0;37m"+'Crear Usuario Gamemaster')
    print(chr(27)+"[1;33m"+'2.- '+ chr(27)+"[0;37m"+'Crear Usuario Jugador')
    print(chr(27)+"[1;33m"+'3.- '+ chr(27)+"[0;37m"+'Volver')
    print()
    opcion = input('Opción: ')
    if opcion == '1':
        creacionUsuario('gamemaster')
    elif opcion == '2':
        creacionUsuario('jugador')
    elif opcion == '3':
        return
    else:
        system('cls')
        print(chr(27)+"[1;31m"+'La Opción ' + opcion + ' Ingresada no es Valida!')
        time.sleep(2)


def creacionUsuario(tipo):  # Paso 2
    system('cls')
    while(True):
        system('cls')
        print(chr(27)+"[1;33m"+'Ingrese un Nombre de Usuario:')
        print()
        nick = input('» ').upper().strip()  # Ingreso Nickname en Mayuscula
        if nick == '' or nick == ' ':
            system('cls')
            print(chr(27)+"[1;3;31m"+'Por Favor, Ingrese un Nombre de Usuario!')
            time.sleep(2)
        else:
            break

    # ---Inicio verificacion de Nickname--->>
    if gamemaster_dao.buscarNombre(nick) or jugador_dao.buscarNombre(nick):
        system('cls')
        print(chr(27)+"[1;31m"+'El nombre: ' + nick + ' ya esta en uso!')
        time.sleep(2)
        return
    # ---Final verificacion de Nickname--->>

    while(True):
        print(chr(27)+"[1;3;33m"+'Cree una Contraseña:')
        print()
        cc = input('» ').strip()  # Ingreso Contraseña
        if cc == '' or cc == ' ':
            system('cls')
            print(chr(27)+"[1;3;31m"+'Debe ingresar una contraseña!')
            time.sleep(2)
        else:
            break

    if tipo == 'gamemaster':
        system('cls')
        print(chr(27)+"[1;3;33m"+'Inserte de que va su historia:')
        print()
        lore = input('» ')
        #
        id_gm = gamemaster_dao.buscarID()
        nuevoGM = t_gamemaster(id_gm, nick, cc, lore)
        gamemaster_dao.crearGM(nuevoGM)
    elif tipo == 'jugador':
        id_jugador = jugador_dao.buscarID()
        nuevoPersonaje = t_jugador(id_jugador, nick, cc)
        jugador_dao.crearJugador(nuevoPersonaje)


# Menu ---------------------------------------->>
while(enFunconamiento):
    time.sleep(1)
    system('cls')
    print(chr(27)+"[1;4;37m"+'Menú'+'\033[0;m')
    print()
    print(chr(
        27)+"[1;3;33m"+'» Seleccione que opcion desea ingresando el numero correspondiente a esta:')
    time.sleep(4)
    system('cls')
    print(chr(27)+"[1;33m"+'1.- ' + chr(27)+"[0;37m"+'Inicio de Sesión')
    print(chr(27)+"[1;33m"+'2.- ' + chr(27)+"[0;37m"+'Crear Usuario')
    print(chr(27)+"[1;33m"+'3.- ' + chr(27)+"[0;37m"+'Salir')
    print()
    seleccion = input('Opción: ')
    # ------------------------------------------>>
    if seleccion == '1':
        ingresoUsuario()
    elif seleccion == '2':
        crearUsuario()
    elif seleccion == '3':
        system('cls')
        print("\033[1;3;36m"+'Cerrando Sistema, Hasta Pronto!' + "\033[0;m")
        enFunconamiento = False
        time.sleep(2) 
        system('cls')
        
    else:
        system('cls')
        print(chr(27)+"[1;3;31m"+'La Opción ' + seleccion + ' Ingresada no es Valida!')
        time.sleep(2);