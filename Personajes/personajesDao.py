from coneccion import coneccion
from beautifultable import BeautifulTable
from Personajes.personajes import personajes
from Razas.razasDao import razasDao

tabla = BeautifulTable()
tabla.columns.header = ['ID', 'Nombre', 'Estado', 'Nivel', 'Inteligencia',
                        'Sabiduria', 'Carisma', 'Experiencia', 'Fuerza', 'Destreza', 'Resistencia', 'ID_Jugador', 'Equipo', 'Raza']
tablaResumen = BeautifulTable()
tablaResumen.columns.header = ['NOMBRE', 'NIVEL', 'INTELIGENCIA', 'SABIDURIA',
                               'CARISMA', 'FUERZA', 'DESTREZA', 'RESISTENCIA', 'RAZA', 'EQUIPO']


class personajesDao:
    def mostrar(self):  # Dibujar tabla Personaje
        tabla.clear()
        for row in coneccion.cursor.execute('select * from PERSONAJE'):
            tabla.rows.append(row)
        print(tabla)

    # Mostrar Tabla Resumen Jugador
    def mostrarPersonajesJugador(self, id_jugador):
        tablaResumen.clear()
        for row in coneccion.cursor.execute('select NOMBRE_PERSONAJE, NIVEL_PERSONAJE, INTELIGENCIA_PERSONAJE, SABIDURIA_PERSONAJE,CARISMA_PERSONAJE,FUERZA,DESTREZA,RESISTENCIA,EQUIPO,RAZA from PERSONAJE where ID_JUGADOR=:1', [id_jugador]):
            tablaResumen.rows.append(row)
        print(tablaResumen)

    def crear(self, task):  # Crear Personaje
        coneccion.cursor.execute('insert into PERSONAJE values(:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14)', [
                                 task.id, task.nombre, task.estado, task.nivel, task.inteligencia, task.sabiduria, task.carisma, task.experiencia, task.fuerza, task.destreza, task.resistencia, task.id_jugador, task.equipo, task.raza])
        coneccion.connection.commit()
        print('Personaje Creado con Exito!')

    def obtenerID(self) -> int:
        for row in coneccion.cursor.execute('select ID_PERSONAJE from PERSONAJE where ID_PERSONAJE=(select max(ID_PERSONAJE) from PERSONAJE)'):
            return int(row[0])+1
