from coneccion import coneccion
from beautifultable import BeautifulTable
from Poderes.poderes import poderes

tabla = BeautifulTable()
tabla.columns.header = ['ID', 'Nombre', 'Detalle']

class poderesDao:
    def mostrar(self):  # Dibujar tabla
        for row in coneccion.cursor.execute('select * from PODER'):
            tabla.rows.append(row)
        print(tabla)