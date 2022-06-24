from coneccion import coneccion
from beautifultable import BeautifulTable
from Personajes.personajes import personajes

tabla = BeautifulTable()
tabla.columns.header = ['ID', 'Nombre', 'Estado', 'Nivel', 'Inteligencia',
                        'Sabiduria', 'Carisma', 'Experiencia', 'Fuerza', 'Destreza', 'Resistencia', 'ID_Jugador', 'Equipo', 'Raza']
tablaResumen = BeautifulTable()
tablaResumen.columns.header = ['NOMBRE','NIVEL','INTELIGENCIA','SABIDURIA','CARISMA','FUERZA','DESTREZA','RESISTENCIA','RAZA','EQUIPO']


class personajesDao:
    def mostrar(self): # Dibujar tabla Personaje
        for row in coneccion.cursor.execute('select * from PERSONAJE'):
            tabla.rows.append(row)
        print(tabla)

    def mostrarPersonajesJugador(self,id_jugador): # Mostrar Tabla Resumen Jugador
        for row in coneccion.cursor.execute('select * from PERSONAJE where ID_JUGADOR=:1',[id_jugador]):
            mostrar = [row[1],row[3],row[4],row[5],row[6],row[8],row[9],row[10],row[13],row[12]]
            tablaResumen.rows.append(mostrar)
        print(tablaResumen)

    def crear(self, task): # Crear Personaje
        coneccion.cursor.execute('insert into PERSONAJE values(:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14)', [
                                 task.id, task.nombre, task.estado, task.nivel, task.inteligencia, task.sabiduria, task.carisma, task.experiencia, task.fuerza, task.destreza, task.resistencia, task.id_jugador, task.equipo, task.raza])
        coneccion.connection.commit()
        print('Personaje Creado con Exito!')

    def obtenerID(self) -> int:
        for row in coneccion.cursor.execute('select ID_PERSONAJE from PERSONAJE where ID_PERSONAJE=(select max(ID_PERSONAJE) from PERSONAJE)'):
            return int(row[0])+1
