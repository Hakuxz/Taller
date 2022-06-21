from coneccion import coneccion
from beautifultable import BeautifulTable
from Habilidades.habilidades import habilidades

tabla = BeautifulTable()
tabla.columns.header = ['ID', 'Nombre', 'Detalle']

class habilidadesDao:
    def mostrar(self):  # Dibujar tabla
        for row in coneccion.cursor.execute('select * from HABILIDAD'):
            tabla.rows.append(row)
        print(tabla)