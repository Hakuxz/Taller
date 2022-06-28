from coneccion import coneccion
from beautifultable import BeautifulTable
from t_jugador import t_jugador

tabla = BeautifulTable()
tabla.columns.header = ['ID','Nombre','Contraseña']

class t_jugadorDAO:
    def crearJugador(self, task):
        coneccion.cursor.execute('insert into JUGADOR values(:1, :2, :3)',[task.id_jugador,task.nombre,task.contrasena])
        coneccion.connection.commit()
        print('Jugador Creado con Exito!')

    def tablas(self): # Dibujar tabla
        tabla.clear()
        for row in coneccion.cursor.execute('select * from JUGADOR'):
            tabla.rows.append(row)
        print(tabla)

    def buscarID(self) -> int:
        for row in coneccion.cursor.execute('select ID_JUGADOR from JUGADOR where ID_JUGADOR=(select max(ID_JUGADOR) from JUGADOR)'):
            return row[0]+1

    def buscarNombre(self,nombre):
        for row in coneccion.cursor.execute('select NOMBRE_JUGADOR from JUGADOR where NOMBRE_JUGADOR=:1',[nombre]):
            if not row:
                return False
            else:
                return True

    def comprobarUsuario(self,nombre,cc):
        for row in coneccion.cursor.execute('select * from JUGADOR'):
            if row[1] == nombre:
                if row[2] == cc:
                    return True
        return False

    def obtenerID(self,nombre):
        for row in coneccion.cursor.execute('select ID_JUGADOR from JUGADOR where NOMBRE_JUGADOR=:1',[nombre]):
            return row[0]
    
    def obtenerNombre(id_jugador) -> str:
        for row in coneccion.cursor.execute('select NOMBRE_JUGADOR from JUGADOR where ID_JUGADOR =:1', [id_jugador]):
            return row[0]

    
