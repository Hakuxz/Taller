from ast import Num
from coneccion import coneccion
from beautifultable import BeautifulTable
from t_jugador import t_jugador

tabla = BeautifulTable()
tabla.columns.header = ['ID','Nombre','Contraseña','Personajes']

class t_jugadorDAO:
    def crearJugador(self, task):
        coneccion.cursor.execute('insert into JUGADOR values(:1, :2, :3, :4)',[task.id_jugador,task.nombre,task.contrasena,task.personajes])
        coneccion.connection.commit()
        print('Jugador Creado con Exito!')

    def comprobar_usuario(self,nombre,cc): # comprobar usuario
        for row in coneccion.cursor.execute('select CONTRASEÑA from JUGADOR where nombre=:1',[nombre]):
            tabla.rows.append(row)
        print(tabla)
        coneccion.cursor.execute('select CONTRASEÑA from JUGADOR where nombre=:1',[nombre])
        #if _cc == cc:
        print(nombre + ' y ' + cc) 
      #  row = coneccion.cursor.fetchone()
      #  if row == None:
      #      print('No se ha encontrado el propietario, por favor verificar el rut e intentar denuevo')
      #  else:
      #      tabla.rows.append(row)
      #  print(tabla)

    def tablas(self): # Dibujar tabla
        for row in coneccion.cursor.execute('select * from JUGADOR'):
            tabla.rows.append(row)
        print(tabla)

    def buscarID(self) -> int:
        if coneccion.cursor.execute('select ID_JUGADOR from JUGADOR where ID_JUGADOR=(select max(ID_JUGADOR) from JUGADOR)') != Num:
            print('ok')
        
