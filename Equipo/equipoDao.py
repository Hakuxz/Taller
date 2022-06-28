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