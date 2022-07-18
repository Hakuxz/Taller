from queue import Empty
from coneccion import coneccion
from beautifultable import BeautifulTable
from Razas.razas import razas
from t_jugadorDAO import t_jugadorDAO

tabla = BeautifulTable()
tabla.columns.header = ['Nombre', 'Fuerza',
                        'Destreza', 'Resistencia', 'Detalle']

class razasDao:
    def mostrar():  # Dibujar tabla
        tabla.clear()
        for row in coneccion.cursor.execute('select NOMBRE_RAZA, FUERZA_RAZA, DESTREZA_RAZA, RESISTENCIA_RAZA, DETALLE_RAZA from RAZA order by ID_RAZA'):
            tabla.rows.append(row)
        print(tabla)

    def mostrarPorID(id_raza): # Buscar en base a la ID de la raza
        tabla.clear()
        for row in coneccion.cursor.execute('select NOMBRE_RAZA, FUERZA_RAZA, DESTREZA_RAZA, RESISTENCIA_RAZA, DETALLE_RAZA from RAZA where ID_RAZA=:1', [id_raza]):
            tabla.rows.append(row)
        print(tabla)
    
    def obtenerLista(): # Mostrar lista ID y Nombre
        listaID = []
        for row in coneccion.cursor.execute('select * from RAZA order by ID_RAZA'):
            listaID.append(str(row[0]))
            print(str(row[0]) + '.- ' + row[1])
        return listaID

    def obtenerListaEdicion(): # Mostrar Lista ID y Nombre de las razas editables
        listaID = []
        for row in coneccion.cursor.execute('select * from RAZA where ID_RAZA > 3 order by ID_RAZA'):
            listaID.append(str(row[0]))
            print(str(row[0]) + '.- ' + row[1])
        return listaID

    def crear(task):
        coneccion.cursor.execute('insert into RAZA values(:1, :2, :3, :4, :5, :6)', [
                                task.id, task.nombre, task.fuerza, task.destreza, task.resistencia, task.detalle])
        coneccion.connection.commit()

    def borrar(id_raza): # Borrar ID
        # lista = []
        # for row in coneccion.cursor.execute('select P.ID_PERSONAJE from PERSONAJE P inner join RAZA R on P.RAZA=R.ID_RAZA where R.ID_RAZA=:1',[id_raza]):
        #     lista.append(row)
        #     if len(lista) == 0:
        #         print('vacio')
        #     else:
        #         print('Lo sentimos no puede borrar una raza la cual posee personajes utilizandola.')
        #         return
        print('Esta seguro que desea borrar la raza: ')
        print('1.- Si, estoy seguro')
        print('2.- No, prefiero conservarla')
        opcion = input('#: ').strip()
        if opcion == '1':
            coneccion.cursor.execute('delete RAZA where ID_RAZA=:1',[id_raza])
            coneccion.connection.commit()
            print('Raza Borrada!')
        elif opcion == '2':
            return
        else:
            print('Valor Ingresado no Valido: ' + opcion)
        
    # Obtener valores:
    def obtenerID():# Obtener la ultima ID y sumar 1
        for row in coneccion.cursor.execute('select ID_RAZA from RAZA where ID_RAZA=(select max(ID_RAZA) from RAZA)'):
            return int(row[0])+1

    def obtenerFuerza(id_raza):
        for row in coneccion.cursor.execute('select FUERZA_RAZA from RAZA where ID_RAZA=:1', [id_raza]):
            return int(row[0])
    
    def obtenerDestreza(id_raza):
        for row in coneccion.cursor.execute('select DESTREZA_RAZA from RAZA where ID_RAZA=:1', [id_raza]):
            return int(row[0])
            
    def obtenerResistencia(id_raza):
        for row in coneccion.cursor.execute('select RESISTENCIA_RAZA from RAZA where ID_RAZA=:1', [id_raza]):
            return int(row[0])

    def obtenerNombre(id_raza) -> str:
        for row in coneccion.cursor.execute('select NOMBRE_RAZA from RAZA where ID_RAZA =:1', [id_raza]):
            return row[0]

    # Modificar Valores:
    def modificarNombre(mod,id_raza):
        coneccion.cursor.execute('update RAZA set NOMBRE_RAZA=:1 where ID_RAZA=:2',[mod,id_raza])
        coneccion.connection.commit()
        print('Nombre Modificado!')

    def modificarFuerza(mod,id_raza):
        coneccion.cursor.execute('update RAZA set FUERZA_RAZA=:1 where ID_RAZA=:2',[mod,id_raza])
        coneccion.connection.commit()
        print('Fuerza Modificada!')

    def modificarDestreza(mod,id_raza):
        coneccion.cursor.execute('update RAZA set DESTREZA_RAZA=:1 where ID_RAZA=:2',[mod,id_raza])
        coneccion.connection.commit()
        print('Destreza Modificada!')

    def modificarResistencia(mod,id_raza):
        coneccion.cursor.execute('update RAZA set RESISTENCIA_RAZA=:1 where ID_RAZA=:2',[mod,id_raza])
        coneccion.connection.commit()
        print('Resistencia Modificada!')

    def modificarDetalle(mod,id_raza):
        coneccion.cursor.execute('update RAZA set DETALLE_RAZA=:1 where ID_RAZA=:2',[mod,id_raza])
        coneccion.connection.commit()
        print('Detalle Modificado!')



    

