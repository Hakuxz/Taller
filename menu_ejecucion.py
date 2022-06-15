import time
import os

# Menu ---------------------------------------->>
def sistemaMenu(tipoMenu, nombre, opcion_1):
    time.sleep(2)
    os.system('cls')
    print('<< Bienvenido' + tipoMenu + ': ' + nombre + ' >>')
    print('<<------------------------------<< Menu >>------------------------------>>')
    print('Seleccione que opcion desea ingresando el numero corrrespondiente a esta:')
    print('1.- ' + opcion_1)
    print('2.- Personajes')
    print('3.- Razas')
    print('4.- Poderes')
    print('5.- Habilidades')
    print('6.- Equipos')
    print('<<------------------------------<< Menu >>------------------------------>>')
    seleccion = input('#: ')