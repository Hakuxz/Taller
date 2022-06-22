from coneccion import coneccion
from beautifultable import BeautifulTable
from Razas.razas import razas

tabla = BeautifulTable()
tabla.columns.header = ['ID', 'Nombre', 'Fuerza',
                        'Destreza', 'Resistencia', 'Detalle']

class razasDao:
    def mostrar(self):  # Dibujar tabla
        for row in coneccion.cursor.execute('select * from RAZA'):
            tabla.rows.append(row)
        print(tabla)

    def crear(self, task):
        coneccion.cursor.execute('insert into RAZA values(:1, :2, :3, :4, :5, :6)', [
                                 task.id_raza, task.nombre, task.fuerza, task.destreza, task.resistencia, task.detalle])
        coneccion.connection.commit()
        print('Raza Creada con Exito!')

    def buscarID(self, id_raza):
        for row in coneccion.cursor.execute('select * from RAZA where ID_RAZA=:1', [id_raza]):
            return row
    
    def buscarFuerza(self, id_raza):
        for row in coneccion.cursor.execute('select FUERZA_RAZA from RAZA where ID_RAZA=:1', [id_raza]):
            return int(row[0])
    
    def buscarDestreza(self, id_raza):
        for row in coneccion.cursor.execute('select DESTREZA_RAZA from RAZA where ID_RAZA=:1', [id_raza]):
            return int(row[0])
            
    def buscarResistencia(self, id_raza):
        for row in coneccion.cursor.execute('select RESISTENCIA_RAZA from RAZA where ID_RAZA=:1', [id_raza]):
            return int(row[0])

    def obtenerLista(self):
        for row in coneccion.cursor.execute('select * from RAZA'):
            print(str(row[0]) + '.- ' + row[1])


    

