import os
import time
from coneccion import coneccion 
from t_jugadorDAO import t_jugadorDAO
#from t_gamemasterDAO import t_gamemasterDAO

coneccion.getStartConnection()
jugador_dao = t_jugadorDAO()
#gamemaster_dao = t_gamemasterDAO()

ingresoSistema = True

nUsuario = ''
ccUsuario = ''

def ingresoUsuario():
    time.sleep(2)
    os.system('cls')
    print('<<------------------------------<< Menu >>------------------------------>>')
    print('Ingrese Nombre de Usuario:')
    nUsuario = input('#: ')
    print('Ingrese Contraseña de Usuario:')
    ccUsuario = input('#: ')
    print('<<------------------------------<< Menu >>------------------------------>>')
    #jugador_dao.comprobarXnombre(nUsuario,ccUsuario)

# Menu ---------------------------------------->>
while(ingresoSistema):
    time.sleep(2)
    os.system('cls')
    print('<<------------------------------<< Menu >>------------------------------>>')
    print('Seleccione que opcion desea ingresando el numero corrrespondiente a esta:')
    print('1.- Ingresar')
    print('2.- Salir')
    print('<<------------------------------<< Menu >>------------------------------>>')
    seleccion = input('#: ')
    if seleccion == '1':
        ingresoUsuario()
        print('ok')
    elif seleccion == '2':
        jugador_dao.tablas()
        print('Cerrando Sistema, Hasta Pronto')
        ingresoSistema = False
    else:
        print('Valor Ingresado no Valido: '+seleccion)


