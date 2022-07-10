from coneccion import coneccion
from beautifultable import BeautifulTable
from Poderes.poderes import poderes

tabla = BeautifulTable()
tabla.columns.header = ['Nombre', 'Detalle']

class poderesDao:
    def mostrar():  # Dibujar tabla
        tabla.clear()
        for row in coneccion.cursor.execute('select * from PODER'):
            mostrar = [row[1],row[2]]
            tabla.rows.append(mostrar)
        print(tabla)