import os
import time
from coneccion import coneccion 
from t_jugador import t_jugador
from t_jugadorDAO import t_jugadorDAO
from t_gamemaster import t_gamemaster
from t_gamemasterDAO import t_gamemasterDAO

coneccion.getStartConnection()
jugador_dao = t_jugadorDAO()
gamemaster_dao = t_gamemasterDAO()

ingresoSistema = True

def ingresoUsuario():
    os.system('cls')
    print('<<---------------------<< Menu Ingresar Usuario >>---------------------->>')
    print('Ingrese su Nombre de Usuario:')
    nnUsuario = input('#: ')
    print('Ingrese su Contraseña:')
    ccUsuario = input('#: ')
    jugador_dao.comprobar_usuario(nnUsuario,ccUsuario)

def crearUsuario():
    os.system('cls')
    print('<<-----------------------<< Menu Crear Usuario >>----------------------->>')
    print('1.- Crear usuario GameMaster')
    print('2.- Crear usuario Jugador')
    opcion = input('#: ')
    if opcion == '1':
        creacionUsuario('gamemaster')
    elif opcion == '2':
        creacionUsuario('jugador')
    else:
        print('Valor Ingresado no Valido: '+seleccion)

def creacionUsuario(tipo):
    os.system('cls')
    print('Seleccione un NickName:')
    nick = input('#: ').lower()

    #---Inicio verificacion de Nickname--->>
    if jugador_dao.buscarNombre(nick):
        print('El Nombre de Usuario ya se encuentra en Uso')
        return
    elif gamemaster_dao.buscarNombre(nick):
        print('El Nombre de Usuario ya se encuentra en Uso')
        return
    #---Final verificacion de Nickname--->>

    print('Cree su Contraseña:')
    cc = input('#: ')

    if tipo == 'gamemaster':
        print('Inserte de que va su historia: ')
        lore = input('#: ')
        id_gm = gamemaster_dao.buscarID()
        nuevoGM = t_gamemaster(id_gm,nick,cc,lore)
        gamemaster_dao.crearGM(nuevoGM)
    elif tipo == 'jugador':
        id_jugador = jugador_dao.buscarID()
        nuevoPersonaje = t_jugador(id_jugador,nick,cc,0)
        jugador_dao.crearJugador(nuevoPersonaje) 

# Menu ---------------------------------------->>
while(ingresoSistema):
    time.sleep(2)
    os.system('cls')
    print('<<-----------------------<< Menu Crear Usuario >>----------------------->>')
    print('Seleccione que opcion desea ingresando el numero corrrespondiente a esta:')
    print('1.- Ingresar Usuario')
    print('2.- Crear Usuario')
    print('3.- Salir')
    print('<<------------------------------<< Menu >>------------------------------>>')
    seleccion = input('#: ')
    #------------------------------------------>>
    if seleccion == '1':
        ingresoUsuario()
    elif seleccion == '2':
        crearUsuario()
    elif seleccion == '3':
        print('Cerrando Sistema, Hasta Pronto')
        ingresoSistema = False
    else:
        print('Valor Ingresado no Valido: '+seleccion)


