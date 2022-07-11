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

    def mostrarPorID(id_equipo): # Buscar en base a la ID de la raza
        tabla.clear()
        for row in coneccion.cursor.execute('select NOMBRE_EQUIPO, TIPO_EQUIPO, DAÑO_EQUIPO, ATAQUE_EQUIPO from EQUIPO where ID_EQUIPO=:1', [id_equipo]):
            tabla.rows.append(row)
        print(tabla)

    def crear(task):
        coneccion.cursor.execute('insert into EQUIPO values(:1, :2, :3, :4, :5)', [
                                task.id, task.nombre, task.tipo, task.dano, task.tipoDano])
        coneccion.connection.commit()
        print('Equipo Creado con Exito!')

    def borrar(id_equipo): # Borrar por ID
        print('Esta seguro que desea borrar el equipamiento: ')
        print('1.- Si, estoy seguro')
        print('2.- No, prefiero conservarlo')
        opcion = input('#: ').strip()
        if opcion == '1':
            coneccion.cursor.execute('delete EQUIPO where ID_EQUIPO=:1',[id_equipo])
            coneccion.connection.commit()
            print('Equipo Borrado!')
        elif opcion == '2':
            return
        else:
            print('Valor Ingresado no Valido: ' + opcion)

    def obtenerNombre(id_equipo): # Entrega el Nombre
        for row in coneccion.cursor.execute('select NOMBRE_EQUIPO from EQUIPO where ID_EQUIPO=:1',[id_equipo]):
            return row[0]

    def obtenerLista():
        for row in coneccion.cursor.execute('select * from EQUIPO order by ID_EQUIPO'):
            print(str(row[0]) + '.- ' + row[1])

    def obtenerID():# Obtener la ultima ID y sumar 1
        for row in coneccion.cursor.execute('select ID_EQUIPO from EQUIPO where ID_EQUIPO=(select max(ID_EQUIPO) from EQUIPO)'):
            return int(row[0])+1

    def cambiarNombre(nuevoNombre,id_equipo):
        coneccion.cursor.execute('update EQUIPO set NOMBRE_EQUIPO=:1 where ID_EQUIPO=:2',[nuevoNombre,id_equipo])
        print('Equipo Modificado Correctamente!')


