from coneccion import coneccion
from beautifultable import BeautifulTable
from Equipo.equipo import equipo

tabla = BeautifulTable()
tabla.columns.header = ['Nombre','Tipo','Daño','Tipo de Daño']

class equipoDao:
    def mostrar():  # Dibujar tabla
        tabla.clear()
        for row in coneccion.cursor.execute('select NOMBRE_EQUIPO, TIPO_EQUIPO, DAÑO_EQUIPO, ATAQUE_EQUIPO from EQUIPO order by ID_EQUIPO'):
            tabla.rows.append(row)
        print(tabla)

    def obtenerNombre(id_equipo): # Entrega el Nombre
        for row in coneccion.cursor.execute('select NOMBRE_EQUIPO from EQUIPO where ID_EQUIPO=:1',[id_equipo]):
            return row[0]

    def obtenerLista():
        for row in coneccion.cursor.execute('select * from EQUIPO order by ID_EQUIPO'):
            print(str(row[0]) + '.- ' + row[1])

    def cambiarNombre(nuevoNombre,id_equipo):
        coneccion.cursor.execute('update EQUIPO set NOMBRE_EQUIPO=:1 where ID_EQUIPO=:2',[nuevoNombre,id_equipo])
        print('Equipo Modificado Correctamente!')


