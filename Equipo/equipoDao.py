from coneccion import coneccion
from beautifultable import BeautifulTable
from Equipo.equipo import equipo

tabla = BeautifulTable()
tabla.columns.header = ['ID', 'Nombre', 'Tipo','Daño','Tipo de Daño']

class equipoDao:
    def mostrar(self):  # Dibujar tabla
        for row in coneccion.cursor.execute('select * from EQUIPO'):
            tabla.rows.append(row)
        print(tabla)