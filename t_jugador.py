<<<<<<< HEAD
class t_jugador:
    def __init__(self,id_jugador,nombre,contrasena,personajes):
        self.__id_jugador = id_jugador
        self.__nombre = nombre
        self.__contrasena = contrasena
        self.__personajes = personajes

    @property # ------------------------------------->>
    def id_jugador(self) -> int:
        return self.__id_jugador

    @property # ------------------------------------->>
    def nombre(self) -> str:
        return self.__nombre
        
    @property # ------------------------------------->>
    def contrasena(self) -> str:
        return self.__contrasena

    @property # ------------------------------------->>
    def personajes(self) -> int:
=======
class t_jugador:
    def __init__(self,id_jugador,nombre,contrasena,personajes):
        self.__id_jugador = id_jugador
        self.__nombre = nombre
        self.__contrasena = contrasena
        self.__personajes = personajes

    @property # ------------------------------------->>
    def id_jugador(self) -> int:
        return self.__id_jugador

    @property # ------------------------------------->>
    def nombre(self) -> str:
        return self.__nombre
        
    @property # ------------------------------------->>
    def contrasena(self) -> str:
        return self.__contrasena

    @property # ------------------------------------->>
    def personajes(self) -> int:
>>>>>>> 6a1aa426e26295b2e64db0e0d0ccef8adcf8fef4
        return self.__personajes