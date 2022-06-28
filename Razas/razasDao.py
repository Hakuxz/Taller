from coneccion import coneccion
from beautifultable import BeautifulTable
from Razas.razas import razas
from t_jugadorDAO import t_jugadorDAO

tabla = BeautifulTable()
tabla.columns.header = ['Nombre', 'Fuerza',
                        'Destreza', 'Resistencia', 'Detalle']

class razasDao:
    def mostrar(self):  # Dibujar tabla
        tabla.clear()
        for row in coneccion.cursor.execute('select * from RAZA'):
            mostrar = [row[1],row[2],row[3],row[4],row[5]]
            tabla.rows.append(mostrar)
        print(tabla)

    def crear(self, task):
        coneccion.cursor.execute('insert into RAZA values(:1, :2, :3, :4, :5, :6)', [
                                 task.id_raza, task.nombre, task.fuerza, task.destreza, task.resistencia, task.detalle])
        coneccion.connection.commit()
        print('Raza Creada con Exito!')

    def buscarID(self, id_raza): # Buscar en base a la ID
        for row in coneccion.cursor.execute('select * from RAZA where ID_RAZA=:1', [id_raza]):
            return row
    
    # Obtener valores:
    def obtenerFuerza(self, id_raza):
        for row in coneccion.cursor.execute('select FUERZA_RAZA from RAZA where ID_RAZA=:1', [id_raza]):
            return int(row[0])
    
    def obtenerDestreza(self, id_raza):
        for row in coneccion.cursor.execute('select DESTREZA_RAZA from RAZA where ID_RAZA=:1', [id_raza]):
            return int(row[0])
            
    def obtenerResistencia(self, id_raza):
        for row in coneccion.cursor.execute('select RESISTENCIA_RAZA from RAZA where ID_RAZA=:1', [id_raza]):
            return int(row[0])

    def obtenerLista(self):
        for row in coneccion.cursor.execute('select * from RAZA'):
            print(str(row[0]) + '.- ' + row[1])

    def obtenerNombre(id_raza) -> str:
        for row in coneccion.cursor.execute('select NOMBRE_RAZA from RAZA where ID_RAZA =:1', [id_raza]):
            return row[0]

    

