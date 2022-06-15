from coneccion import coneccion
from beautifultable import BeautifulTable
from t_jugador import t_jugador

tabla = BeautifulTable()
tabla.columns.header = ['ID','Nombre','Cc']

class t_jugadorDAO:
    def comprobarXnombre(self,nombre,cc) -> None: # ------------------------------------------>>
        _cc = coneccion.cursor.execute('select CONTRASENA from PERSONAJE where nombre=:1',[nombre])
        if _cc == cc:
            print('nombre y cc') 
        row = coneccion.cursor.fetchone()
        if row == None:
            print('No se ha encontrado el propietario, por favor verificar el rut e intentar denuevo')
        else:
            tabla.rows.append(row)
        print(tabla)

    def tablas(self) -> None:  # -------------------------------------------->> Dibujar tabla
        for row in coneccion.cursor.execute('select * from JUGADOR'):
            tabla.rows.append(row)
        print(tabla)

