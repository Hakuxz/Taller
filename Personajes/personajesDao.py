from coneccion import coneccion
from beautifultable import BeautifulTable
from Personajes.personajes import personajes

tabla = BeautifulTable()
tabla.columns.header = ['ID', 'Nombre', 'Estado', 'Nivel', 'Inteligencia',
                        'Sabiduria', 'Carisma', 'Experiencia', 'Fuerza', 'Destreza', 'Resistencia', 'ID_Jugador', 'Equipo', 'Raza']


class personajesDao:
    def mostrar(self): # Dibujar tabla Personaje
        for row in coneccion.cursor.execute('select * from PERSONAJE'):
            tabla.rows.append(row)
        print(tabla)

    def crear(self, task): # Crear Personaje
        coneccion.cursor.execute('insert into PERSONAJE values(:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14)', [
                                 task.id, task.nombre, task.estado, task.nivel, task.inteligencia, task.sabiduria, task.carisma, task.experiencia, task.fuerza, task.destreza, task.resistencia, task.id_jugador, task.equipo, task.raza])
        coneccion.connection.commit()
        print('Personaje Creado con Exito!')

    def buscarID(self) -> int:
        for row in coneccion.cursor.execute('select ID_PERSONAJE from PERSONAJE where ID_PERSONAJE=(select max(ID_PERSONAJE) from PERSONAJE)'):
            return int(row[0]+1)
