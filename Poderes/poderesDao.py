from coneccion import coneccion
from beautifultable import BeautifulTable
from Poderes.poderes import poderes

tabla = BeautifulTable()
tabla.columns.header = ['NOMBRE','DESCRIPCIÓN','RAZA']

class poderesDao:
    def mostrar():  # Dibujar tabla
        tabla.clear()
        for row in coneccion.cursor.execute('select P.NOMBRE_PODER, P.DETALLE_PODER, R.NOMBRE_RAZA from PODER P inner join RAZA R on P.RAZA_PODER=R.ID_RAZA order by P.ID_PODER'):
            tabla.rows.append(row)
        print(tabla)

    def mostrarPorID(id_poder):  # Dibujar tabla buscada mediante la ID
        tabla.clear()
        for row in coneccion.cursor.execute('select P.NOMBRE_PODER, P.DETALLE_PODER, R.NOMBRE_RAZA from PODER P inner join RAZA R on P.RAZA_PODER=R.ID_RAZA where P.ID_PODER=:1 order by P.ID_PODER',[id_poder]):
            tabla.rows.append(row)
        print(tabla)

    def obtenerListaAcotada(): # Mostrar Lista ID y Nombre de los poderes editables
        listaID = []
        for row in coneccion.cursor.execute('select * from PODER where ID_PODER > 3 order by ID_PODER'):
            listaID.append(str(row[0]))
            print(str(row[0]) + '.- ' + row[1])
        return listaID

    def crear(task): # Crear Poder
        coneccion.cursor.execute('insert into PODER values(:1, :2, :3, :4)', [
                                task.id, task.nombre, task.detalle, task.raza])
        coneccion.connection.commit()
        print('Poder Creado con Exito!')

    def obtenerID():# Obtener la ultima ID y sumar 1
        for row in coneccion.cursor.execute('select ID_PODER from PODER where ID_PODER=(select max(ID_PODER) from PODER)'):
            return int(row[0])+1

    def obtenerLista():
        listaID = []
        for row in coneccion.cursor.execute('select * from PODER order by ID_PODER'):
            listaID.append(str(row[0]))
            print(str(row[0]) + '.- ' + row[1])
        return listaID

    def obtenerNombre(id_equipo): # Entrega el Nombre
        for row in coneccion.cursor.execute('select NOMBRE_PODER from PODER where ID_PODER=:1',[id_equipo]):
            return row[0]

    def borrar(id_poder): # Borrar por ID
        print('Esta seguro que desea borrar el Poder: ')
        print('1.- Si, estoy seguro')
        print('2.- No, prefiero conservarlo')
        opcion = input('#: ').strip()
        if opcion == '1':
            coneccion.cursor.execute('delete PODER where ID_PODER=:1',[id_poder])
            coneccion.connection.commit()
            print('Poder Borrado!')
        elif opcion == '2':
            return
        else:
            print('Valor Ingresado no Valido: ' + opcion)

    def modificarDetalle(mod,id_poder):
        coneccion.cursor.execute('update PODER set DETALLE_PODER=:1 where ID_PODER=:2',[mod,id_poder])
        coneccion.connection.commit()
        print('Descripción Modificada!')
