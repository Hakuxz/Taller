from coneccion import coneccion
from beautifultable import BeautifulTable
from Equipo.equipo import equipo

tabla = BeautifulTable()
tabla.columns.header = ['Nombre','Tipo','Daño','Tipo de Daño']

class equipoDao:
    def mostrar(self):  # Dibujar tabla
        tabla.clear()
        for row in coneccion.cursor.execute('select * from EQUIPO'):
            mostrar = [row[1],row[2],row[3],row[4]]
            tabla.rows.append(mostrar)
        print(tabla)

    def obtenerNombre(id_equipo): # Entrega el Nombre
        for row in coneccion.cursor.execute('select NOMBRE_EQUIPO from EQUIPO where ID_EQUIPO=:1',[id_equipo]):
            return row[0]

    def obtenerLista():
        for row in coneccion.cursor.execute('select * from EQUIPO'):
            print(str(row[0]) + '.- ' + row[1])
