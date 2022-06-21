from coneccion import coneccion
from beautifultable import BeautifulTable
from Personajes.personajes import personajes

tabla = BeautifulTable()
tabla.columns.header = ['ID', 'Nombre','Estado','Nivel','Inteligencia','Sabiduria','Carisma','Experiencia','Fuerza','Destreza','Resistencia']

class personajesDao:
    def mostrar(self):  # Dibujar tabla
        for row in coneccion.cursor.execute('select * from PERSONAJE'):
            tabla.rows.append(row)
        print(tabla)