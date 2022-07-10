from coneccion import coneccion
from beautifultable import BeautifulTable
from Habilidades.habilidades import habilidades

tabla = BeautifulTable()
tabla.columns.header = ['Nombre', 'Detalle']

class habilidadesDao:
    def mostrar():  # Dibujar tabla
        tabla.clear()
        for row in coneccion.cursor.execute('select * from HABILIDAD'):
            mostrar = [row[1],row[2]]
            tabla.rows.append(mostrar)
        print(tabla)