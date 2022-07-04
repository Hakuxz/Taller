from coneccion import coneccion
from beautifultable import BeautifulTable
from Estados.estados import estados

tabla = BeautifulTable()
tabla.columns.header = ['ID', 'Nombre', 'Descripcion']

class estadosDao:
    def mostrar(self):  # Dibujar tabla
        tabla.clear()
        for row in coneccion.cursor.execute('select * from ESTADOS'):
            tabla.rows.append(row)
        print(tabla)

    def obtenerNombre(id_estado): # Entrega el Nombre
        for row in coneccion.cursor.execute('select NOMBRE from ESTADOS where ID_ESTADO=:1',[id_estado]):
            return row[0]

    def obtenerLista():
        for row in coneccion.cursor.execute('select * from ESTADOS'):
            print(str(row[0]) + '.- ' + row[1])
