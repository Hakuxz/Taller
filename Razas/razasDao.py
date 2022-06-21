from coneccion import coneccion
from beautifultable import BeautifulTable
from Razas.razas import razas

tabla = BeautifulTable()
tabla.columns.header = ['ID', 'Nombre', 'Fuerza',
                        'Destreza', 'Resistencia', 'Detalle', 'Habilidad', 'Poder']


class razasDao:
    def mostrar(self):  # Dibujar tabla
        for row in coneccion.cursor.execute('select * from RAZA'):
            tabla.rows.append(row)
        print(tabla)

    def crear(self, task):
        coneccion.cursor.execute('insert into RAZA values(:1, :2, :3, :4, :5, :6, :7, :8)', [
                                 task.id_raza, task.nombre, task.fuerza, task.destreza, task.resistencia, task.detalle, task.habilidad, task.poder])
        coneccion.connection.commit()
        print('Raza Creada con Exito!')

    def obtenerRaza(self, raza):
        for row in coneccion.cursor.execute('select * from RAZA where ID_RAZA=:1', [raza]):
            return row
