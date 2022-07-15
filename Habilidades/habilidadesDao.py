from coneccion import coneccion
from beautifultable import BeautifulTable
from Habilidades.habilidades import habilidades

tabla = BeautifulTable()
tabla.columns.header = ['NOMBRE', 'DESCRIPCIÓN','RAZA']

class habilidadesDao:
    def mostrar():  # Dibujar tabla
        tabla.clear()
        for row in coneccion.cursor.execute('select H.NOMBRE_HABILIDAD, H.DETALLE_HABILIDAD, R.NOMBRE_RAZA from HABILIDAD H inner join RAZA R on H.RAZA_HABILIDAD=R.ID_RAZA order by ID_HABILIDAD'):
            tabla.rows.append(row)
        print(tabla)

    def mostrarPorID(id_habilidad):  # Dibujar tabla buscada mediante la ID
        tabla.clear()
        for row in coneccion.cursor.execute('select H.NOMBRE_HABILIDAD, H.DETALLE_HABILIDAD, R.NOMBRE_RAZA from HABILIDAD H inner join RAZA R on H.RAZA_HABILIDAD=R.ID_RAZA where H.ID_HABILIDAD=:1',[id_habilidad]):
            tabla.rows.append(row)
        print(tabla)

    def obtenerListaAcotada(): # Mostrar Lista ID y Nombre de los poderes editables
        listaID = []
        for row in coneccion.cursor.execute('select * from HABILIDAD where ID_HABILIDAD > 7 order by ID_HABILIDAD'):
            listaID.append(str(row[0]))
            print(str(row[0]) + '.- ' + row[1])
        return listaID

    def crear(task): # Crear Poder
        coneccion.cursor.execute('insert into HABILIDAD values(:1, :2, :3, :4)', [
                                task.id, task.nombre, task.detalle, task.raza])
        coneccion.connection.commit()
        print('Habilidad Creada con Exito!')

    def obtenerID():# Obtener la ultima ID y sumar 1
        for row in coneccion.cursor.execute('select ID_HABILIDAD from HABILIDAD where ID_HABILIDAD=(select max(ID_HABILIDAD) from HABILIDAD)'):
            return int(row[0])+1

    def obtenerLista():
        listaID = []
        for row in coneccion.cursor.execute('select * from HABILIDAD order by ID_HABILIDAD'):
            listaID.append(str(row[0]))
            print(str(row[0]) + '.- ' + row[1])
        return listaID

    def obtenerNombre(id_habilidad): # Entrega el Nombre
        for row in coneccion.cursor.execute('select NOMBRE_HABILIDAD from HABILIDAD where ID_HABILIDAD=:1',[id_habilidad]):
            return row[0]

    def borrar(id_habilidad): # Borrar por ID
        print('Esta seguro que desea borrar el Poder: ')
        print('1.- Si, estoy seguro')
        print('2.- No, prefiero conservarlo')
        opcion = input('#: ').strip()
        if opcion == '1':
            coneccion.cursor.execute('delete HABILIDAD where ID_HABILIDAD=:1',[id_habilidad])
            coneccion.connection.commit()
            print('Hablidad Borrado!')
        elif opcion == '2':
            return
        else:
            print('Valor Ingresado no Valido: ' + opcion)

    def modificarDetalle(mod,id_habilidad):
        coneccion.cursor.execute('update HABILIDAD set DETALLE_HABILIDAD=:1 where ID_HABILIDAD=:2',[mod,id_habilidad])
        coneccion.connection.commit()
        print('Descripción Modificada!')
