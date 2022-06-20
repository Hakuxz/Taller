import time
import os

# Menu ---------------------------------------->>
class menu_ejecucion():
    def __init__(self,enFuncionamiento,tipoMenu,nombre,opcion_1):
        while(enFuncionamiento):
            time.sleep(2)
            os.system('cls')
            print('<< Bienvenido ' + nombre + ' >>')
            print('<<------------------------------<< Menu >>------------------------------>>')
            print('Seleccione que opcion desea ingresando el numero corrrespondiente a esta:')
            print('1.- ' + opcion_1)
            print('2.- Personajes')
            print('3.- Razas')
            print('4.- Poderes')
            print('5.- Habilidades')
            print('6.- Equipos')
            print('7.- Salir')
            print('<<------------------------------<< Menu >>------------------------------>>')
            seleccion = input('#: ')
            if seleccion == '1':
                pass
            elif seleccion == '2':
                pass
            elif seleccion == '3':
                pass
            elif seleccion == '4':
                pass
            elif seleccion == '5':
                pass
            elif seleccion == '6':
                pass
            elif seleccion == '7':
                print('Hasta Luego ' + nombre)
                enFuncionamiento = False
