from coneccion import coneccion
from beautifultable import BeautifulTable
from t_jugador import t_jugador

tabla = BeautifulTable()
tabla.columns.header = ['ID','Nombre','Contraseña','Personajes']

class t_jugadorDAO:
    def crearJugador(self, task):
        coneccion.cursor.execute('insert into JUGADOR values(:1, :2, :3, :4)',[task.id_jugador,task.nombre,task.contrasena,task.personajes])
        coneccion.connection.commit()
        print('Jugador Creado con Exito!')

    def tablas(self): # Dibujar tabla
        for row in coneccion.cursor.execute('select * from JUGADOR'):
            tabla.rows.append(row)
        print(tabla)

    def buscarID(self) -> int:
        for row in coneccion.cursor.execute('select ID_JUGADOR from JUGADOR where ID_JUGADOR=(select max(ID_JUGADOR) from JUGADOR)'):
            return row[0]+1

    def buscarNombre(self,nombre):
        for row in coneccion.cursor.execute('select NOMBRE_JUGADOR from JUGADOR'):
            for i in row:
                if i == nombre:
                    return True
                else:
                    return False

    def comprobarUsuario(self,nombre,cc):
        for row in coneccion.cursor.execute('select * from JUGADOR'):
            if row[1] == nombre:
                if row[2] == cc:
                    return True
                else:
                    print('Usuario No Valido')
                    return False
            else:
                print('Nickname Ingresado No Valido')
                return False

