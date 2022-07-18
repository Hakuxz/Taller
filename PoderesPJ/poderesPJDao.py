from coneccion import coneccion
from beautifultable import BeautifulTable
from PoderesPJ.poderesPJ import poderesPJ

tabla = BeautifulTable()
tabla.columns.header = ['PODER']

class poderesPJDao:
    def crear(task):  # Crear Poder
        coneccion.cursor.execute('insert into PODERESPJ values(:1, :2)', [
            task.personaje, task.poder])
        coneccion.connection.commit()
        print('Exito!')

    def mostrar(id_personaje):
        tabla.clear()
        for row in coneccion.cursor.execute('select O.NOMBRE_PODER from PODERESPJ J inner join PERSONAJE P on J.ID_PJ=P.ID_PERSONAJE inner join PODER O on J.ID_PODER=O.ID_PODER where J.ID_PJ=:1',[id_personaje]):
            tabla.rows.append(row)
        print(tabla)
