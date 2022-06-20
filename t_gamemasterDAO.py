<<<<<<< HEAD
from inspect import _void
from coneccion import coneccion
from beautifultable import BeautifulTable
from t_gamemaster import t_gamemaster

tabla = BeautifulTable()
tabla.columns.header = ['ID','Nombre','Contraseña','Historia']

class t_gamemasterDAO:
    def crearGM(self, task):
        coneccion.cursor.execute('insert into GAMEMASTER values(:1, :2, :3, :4)',[task.id_gm,task.nombre,task.contrasena,task.historias])
        coneccion.connection.commit()
        print('GM Creado con Exito!')

    def tablas(self): # Dibujar tabla
        for row in coneccion.cursor.execute('select * from GAMEMASTER'):
            tabla.rows.append(row)
        print(tabla)

    def buscarID(self) -> int:
        for row in coneccion.cursor.execute('select ID_GAMEMASTER from GAMEMASTER where ID_GAMEMASTER=(select max(ID_GAMEMASTER) from GAMEMASTER)'):
            return row[0]+1
    
    def buscarNombre(self,nombre):
        for row in coneccion.cursor.execute('select NOMBRE_GAMEMASTER from GAMEMASTER'):
            for i in row:
                if i == nombre:
                    return True
                else:
                    return False

    def comprobarUsuario(self,nombre,cc):
        for row in coneccion.cursor.execute('select * from GAMEMASTER'):
            if row[1] == nombre:
                if row[2] == cc:
                    return True
                else:
                    print('Usuario No Valido')
                    return False
            else:
                print('Nickname Ingresado No Valido')
                return False
=======
from inspect import _void
from coneccion import coneccion
from beautifultable import BeautifulTable
from t_gamemaster import t_gamemaster

tabla = BeautifulTable()
tabla.columns.header = ['ID','Nombre','Contraseña','Historia']

class t_gamemasterDAO:
    def crearGM(self, task):
        coneccion.cursor.execute('insert into GAMEMASTER values(:1, :2, :3, :4)',[task.id_gm,task.nombre,task.contrasena,task.historias])
        coneccion.connection.commit()
        print('GM Creado con Exito!')

    def tablas(self): # Dibujar tabla
        for row in coneccion.cursor.execute('select * from GAMEMASTER'):
            tabla.rows.append(row)
        print(tabla)

    def buscarID(self) -> int:
        for row in coneccion.cursor.execute('select ID_GAMEMASTER from GAMEMASTER where ID_GAMEMASTER=(select max(ID_GAMEMASTER) from GAMEMASTER)'):
            return row[0]+1
    
    def buscarNombre(self,nombre):
        for row in coneccion.cursor.execute('select NOMBRE_GAMEMASTER from GAMEMASTER'):
            for i in row:
                if i == nombre:
                    return True
                else:
                    return False

    def comprobarUsuario(self,nombre,cc):
        for row in coneccion.cursor.execute('select * from GAMEMASTER'):
            if row[1] == nombre:
                if row[2] == cc:
                    return True
                else:
                    print('Usuario No Valido')
                    return False
            else:
                print('Nickname Ingresado No Valido')
                return False
>>>>>>> 6a1aa426e26295b2e64db0e0d0ccef8adcf8fef4
