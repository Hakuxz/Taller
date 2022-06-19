import os
import time
from coneccion import coneccion 
from t_jugador import t_jugador
from t_jugadorDAO import t_jugadorDAO
#from t_gamemaster import t_gamemaster
#from t_gamemasterDAO import t_gamemasterDAO

coneccion.getStartConnection()
jugador_dao = t_jugadorDAO()
#gamemaster_dao = t_gamemasterDAO()

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
    print('Seleccione un NickName:')
    nick = input('#: ').upper()
    print('Cree su Contraseña:')
    cc = input('#: ')
    id_j = jugador_dao.buscarID()
    nuevoPersonaje = t_jugador(id_j,nick,cc,0)
    jugador_dao.crearJugador(nuevoPersonaje)

# Menu ---------------------------------------->>
while(ingresoSistema):
    time.sleep(2)
    os.system('cls')
    print('<<-----------------------<< Menu Crear Usuario >>----------------------->>')
    print('Seleccione que opcion desea ingresando el numero corrrespondiente a esta:')
    print('1.- Ingresar')
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


