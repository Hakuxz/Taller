from multiprocessing import connection
from Equipo.equipoDao import equipoDao
from Estados.estadosDao import estadosDao
from coneccion import coneccion
from beautifultable import BeautifulTable
from Razas.razasDao import razasDao
from t_jugadorDAO import t_jugadorDAO

tabla = BeautifulTable()
tabla.columns.header = ['ID', 'Nombre', 'Estado', 'Nivel', 'Inteligencia',
                        'Sabiduria', 'Carisma', 'Experiencia', 'Fuerza', 'Destreza', 'Resistencia', 'ID_Jugador', 'Equipo', 'Raza']
tablaJG = BeautifulTable()
tablaJG.columns.header = ['NOMBRE', 'NIVEL', 'INTELIGENCIA', 'SABIDURIA',
                               'CARISMA', 'FUERZA', 'DESTREZA', 'RESISTENCIA', 'RAZA', 'EQUIPO']
tablaGM = BeautifulTable()
tablaGM.columns.header = ['NOMBRE', 'ESTADO', 'NIVEL', 'EXP', 'JUGADOR', 'RAZA', 'EQUIPO']


class personajesDao:
    def mostrar(self):  # Dibujar tabla Personaje
        tabla.clear()
        for row in coneccion.cursor.execute('select * from PERSONAJE'):
            tabla.rows.append(row)
        print(tabla)

    def mostrarPersonajesGamemaster():  # Mostrar Tabla Resumen GameMaster
        tablaGM.clear()
        for row in coneccion.cursor.execute('select P.NOMBRE_PERSONAJE, S.NOMBRE, P.NIVEL_PERSONAJE, P.EXPERIENCIA, P.ID_JUGADOR, R.NOMBRE_RAZA, E.NOMBRE_EQUIPO from PERSONAJE P inner join RAZA R on P.RAZA=R.ID_RAZA inner join EQUIPO E on P.EQUIPO=E.ID_EQUIPO inner join ESTADOS S on ESTADO_PERSONAJE=ID_ESTADO order by P.ID_PERSONAJE'):
            tablaGM.rows.append(row)
        print(tablaGM)

    def obtenerPersonajeJugador(id_jugador): #Obtener valores de un personaje mediante su ID : JG
        tablaJG.clear()
        for row in coneccion.cursor.execute('select P.NOMBRE_PERSONAJE, P.NIVEL_PERSONAJE, P.INTELIGENCIA_PERSONAJE, P.SABIDURIA_PERSONAJE, P.CARISMA_PERSONAJE, P.FUERZA, P.DESTREZA, P.RESISTENCIA, R.NOMBRE_RAZA, E.NOMBRE_EQUIPO from PERSONAJE P inner join RAZA R on P.RAZA=R.ID_RAZA inner join EQUIPO E on P.EQUIPO=E.ID_EQUIPO where ID_JUGADOR=:1 order by ID_PERSONAJE',[id_jugador]):
            tablaJG.rows.append(row)
        print(tablaJG)

    def obtenerPersonajePorID(id_personaje): #Obtener valores de un personaje mediante su ID : GM
        tablaGM.clear()
        for row in coneccion.cursor.execute('select P.NOMBRE_PERSONAJE, S.NOMBRE, P.NIVEL_PERSONAJE, P.EXPERIENCIA, P.ID_JUGADOR, R.NOMBRE_RAZA, E.NOMBRE_EQUIPO from PERSONAJE P inner join RAZA R on P.RAZA=R.ID_RAZA inner join EQUIPO E on P.EQUIPO=E.ID_EQUIPO inner join ESTADOS S on ESTADO_PERSONAJE=ID_ESTADO where ID_PERSONAJE=:1 order by ID_PERSONAJE',[id_personaje]):
            tablaGM.rows.append(row)
        print(tablaGM)

    def crear(task):  # Crear Personaje
        coneccion.cursor.execute('insert into PERSONAJE values(:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14)', [
                                 task.id, task.nombre, task.estado, task.nivel, task.inteligencia, task.sabiduria, task.carisma, task.experiencia, task.fuerza, task.destreza, task.resistencia, task.id_jugador, task.equipo, task.raza])
        coneccion.connection.commit()
        print('Personaje Creado con Exito!')

    def obtenerID() -> int:
        for row in coneccion.cursor.execute('select ID_PERSONAJE from PERSONAJE where ID_PERSONAJE=(select max(ID_PERSONAJE) from PERSONAJE)'):
            return int(row[0])+1

    def obtenerEstado(id_personaje):
        for row in coneccion.cursor.execute('select ESTADO_PERSONAJE from PERSONAJE where ID_PERSONAJE=:1',[id_personaje]):
            return int(row[0])

    def obtenerLista():
        for row in coneccion.cursor.execute('select * from PERSONAJE'):
            print(str(row[0]) + '.- ' + row[1])

    def obtenerListaPersonaje(id_jugador):
        for row in coneccion.cursor.execute('select * from PERSONAJE where ID_JUGADOR=:1',[id_jugador]):
            print(str(row[0]) + '.- ' + row[1])

    def obtenerExperiencia(id_personaje) -> int:
        for row in coneccion.cursor.execute('select EXPERIENCIA from PERSONAJE where ID_PERSONAJE=:1',[id_personaje]):
            return row[0]

    def obtenerNivel(id_persoanje) -> int:
        for row in coneccion.cursor.execute('select NIVEL_PERSONAJE from PERSONAJE where ID_PERSONAJE=:1',[id_persoanje]):
            return row[0]

    def otorgarExp(experiencia,id_personaje,nivelActual):
        niveles = [30,55,70,100,150]
        for i in niveles:
            if nivelActual == 1 and experiencia >= niveles[0]:
                expActual = experiencia - niveles[0]    
                coneccion.cursor.execute('update PERSONAJE set NIVEL_PERSONAJE=:1 where ID_PERSONAJE=:1',[(nivelActual+1),id_personaje])        
                coneccion.cursor.execute('update PERSONAJE set EXPERIENCIA=:1 where ID_PERSONAJE=:1',[expActual,id_personaje])
                coneccion.connection.commit()
                print('Experiencia otorgada con Exito!')
                break
            if nivelActual == 2 and experiencia >= niveles[1]:
                expActual = experiencia - niveles[1]    
                coneccion.cursor.execute('update PERSONAJE set NIVEL_PERSONAJE=:1 where ID_PERSONAJE=:1',[(nivelActual+1),id_personaje])        
                coneccion.cursor.execute('update PERSONAJE set EXPERIENCIA=:1 where ID_PERSONAJE=:1',[expActual,id_personaje])
                coneccion.connection.commit()
                print('Experiencia otorgada con Exito!')
                break
            if nivelActual == 3 and experiencia >= niveles[2]:
                expActual = experiencia - niveles[2]    
                coneccion.cursor.execute('update PERSONAJE set NIVEL_PERSONAJE=:1 where ID_PERSONAJE=:1',[(nivelActual+1),id_personaje])        
                coneccion.cursor.execute('update PERSONAJE set EXPERIENCIA=:1 where ID_PERSONAJE=:1',[expActual,id_personaje])
                coneccion.connection.commit()
                print('Experiencia otorgada con Exito!')
                break
            if nivelActual == 4 and experiencia >= niveles[3]:
                expActual = experiencia - niveles[3]    
                coneccion.cursor.execute('update PERSONAJE set NIVEL_PERSONAJE=:1 where ID_PERSONAJE=:1',[(nivelActual+1),id_personaje])        
                coneccion.cursor.execute('update PERSONAJE set EXPERIENCIA=:1 where ID_PERSONAJE=:1',[expActual,id_personaje])
                coneccion.connection.commit()
                print('Experiencia otorgada con Exito!')
                break
            if nivelActual == 5 and experiencia >= niveles[4]:
                expActual = experiencia - niveles[4]    
                coneccion.cursor.execute('update PERSONAJE set NIVEL_PERSONAJE=:1 where ID_PERSONAJE=:1',[(nivelActual+1),id_personaje])        
                coneccion.cursor.execute('update PERSONAJE set EXPERIENCIA=:1 where ID_PERSONAJE=:1',[expActual,id_personaje])
                coneccion.connection.commit()
                print('Experiencia otorgada con Exito!')
                break
        coneccion.cursor.execute('update PERSONAJE set EXPERIENCIA=:1 where ID_PERSONAJE=:1',[experiencia,id_personaje])
        coneccion.connection.commit()
        print('Experiencia otorgada con Exito!')

    def cambiarEstado(id_personaje):
        print('Seleccione el estado que desea otorgar al personaje: ')
        estadosDao.obtenerLista()
        opcion = input('#: ')
        if not opcion:
            print('Valor Ingresado no Valido: ' + opcion)
        else:
            try:
                coneccion.cursor.execute('update PERSONAJE set ESTADO_PERSONAJE=:1 where ID_PERSONAJE=:1',[opcion,id_personaje])
                coneccion.connection.commit()
                print('Estado Cambiado Correctamente!')
            except:
                print('Valor Ingresado no Valido: ' + opcion)

    def borrar(id_personaje):
        print('Esta seguro que desea borrar el personaje: ')
        print('1.- Si, estoy seguro')
        print('2.- No, prefiero conservarlo')
        opcion = input('#: ')
        if opcion == '1':
            coneccion.cursor.execute('delete PERSONAJE where ID_PERSONAJE=:1',[id_personaje])
            coneccion.connection.commit()
            print('Personaje Borrado!')
        elif opcion == '2':
            return
        else:
            print('Valor Ingresado no Valido: ' + opcion)

    def modificarEquipo(id_personaje,estado):
        if estado == 0:
            print('No puede modificar un personaje que posea el Estado: Muerto')
        elif estado == 1:
            print('Seleccione que arma desea para su personaje: ')
            equipoDao.obtenerLista()
            opcion = input('#: ')
            if not opcion:
                print('Valor Ingresado no Valido: ' + opcion)
                return
            else:
                coneccion.cursor.execute('update PERSONAJE set EQUIPO=:1 where ID_PERSONAJE=:2',[opcion,id_personaje])
                coneccion.connection.commit()
                print('Equipo Modificado!')
        else:
            print('Valor Ingresado no Valido: ' + str(estado))
        

