from coneccion import coneccion
from beautifultable import BeautifulTable
from HabilidadesPJ.habilidadesPJ import habilidadesPJ

tabla = BeautifulTable()
tabla.columns.header = ['HABILIDADES']

class habilidadesPJDao:
    def crear(task):  # Crear Poder
        coneccion.cursor.execute('insert into HABILIDADESPJ values(:1, :2)', [
            task.personaje, task.habilidad])
        coneccion.connection.commit()
        print('Exito!')

    def mostrar(id_personaje):
        tabla.clear()
        for row in coneccion.cursor.execute('select H.NOMBRE_HABILIDAD from HABILIDADESPJ J inner join PERSONAJE P on J.ID_PERSONAJE=P.ID_PERSONAJE inner join HABILIDAD H on J.ID_HABILIDAD=H.ID_HABILIDAD where J.ID_PERSONAJE=:1',[id_personaje]):
            tabla.rows.append(row)
        print(tabla)
