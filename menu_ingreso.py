import os
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
    os.system('cls')
    print('>> Ingresar Usuario >>')
    print('Ingrese su Nombre de Usuario:')
    nnUsuario = input('#: ').upper().strip() # Ingreso Nickname en Mayuscula
    print('Ingrese su Contraseña:')
    ccUsuario = input('#: ').strip()
    if jugador_dao.comprobarUsuario(nnUsuario,ccUsuario):
        menu = menu_jugador(enFunconamiento,nnUsuario,jugador_dao.obtenerID(nnUsuario))
    elif gamemaster_dao.comprobarUsuario(nnUsuario,ccUsuario):
        menu = menu_gamemaster(enFunconamiento,nnUsuario,jugador_dao.obtenerID(nnUsuario))
    else:
        print('Los Datos Ingresado no Coinciden')

def crearUsuario(): # Paso 1
    os.system('cls')
    print('>> Crear Usuario >>')
    print('1.- Crear usuario GameMaster')
    print('2.- Crear usuario Jugador')
    print('3.- Volver')
    opcion = input('#: ')
    if opcion == '1':
        creacionUsuario('gamemaster')
    elif opcion == '2':
        creacionUsuario('jugador')
    elif opcion == '3':
        return
    else:
        print('Valor Ingresado no Valido: '+seleccion)

def creacionUsuario(tipo): # Paso 2
    os.system('cls')
    print('Seleccione un NickName:')
    nick = input('#: ').upper().strip() # Ingreso Nickname en Mayuscula

    #---Inicio verificacion de Nickname--->>
    if gamemaster_dao.buscarNombre(nick) or jugador_dao.buscarNombre(nick):
        print('El Nombre de Usuario ya se encuentra en Uso')
        return
    #---Final verificacion de Nickname--->>

    print('Cree su Contraseña:')
    cc = input('#: ').strip() # Ingreso Contraseña

    if tipo == 'gamemaster':
        print('Inserte de que va su historia:')
        lore = input('#: ')
        #
        id_gm = gamemaster_dao.buscarID()
        nuevoGM = t_gamemaster(id_gm,nick,cc,lore)
        gamemaster_dao.crearGM(nuevoGM)
    elif tipo == 'jugador':
        id_jugador = jugador_dao.buscarID()
        nuevoPersonaje = t_jugador(id_jugador,nick,cc)
        jugador_dao.crearJugador(nuevoPersonaje)

# Menu ---------------------------------------->>
while(enFunconamiento):
    time.sleep(1)
    os.system('cls')
    print('>>  Menu >>')
    print('Seleccione que opcion desea ingresando el numero corrrespondiente a esta:')
    print('1.- Ingresar Usuario')
    print('2.- Crear Usuario')
    print('3.- Salir')
    print('>> Menu >>')
    seleccion = input('#: ')
    #------------------------------------------>>
    if seleccion == '1':
        ingresoUsuario()
    elif seleccion == '2':
        crearUsuario()
    elif seleccion == '3':
        os.system('cls')
        print('Cerrando Sistema, Hasta Pronto')
        enFunconamiento = False
    else:
        print('Valor Ingresado no Valido: '+seleccion)
        time.sleep(1)