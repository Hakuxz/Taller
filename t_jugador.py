class t_jugador:
    def __init__(self,id_jugador,nombre,contrasena):
        self.__id_jugador = id_jugador
        self.__nombre = nombre
        self.__contrasena = contrasena

    @property # ------------------------------------->>
    def id_jugador(self) -> int:
        return self.__id_jugador

    @property # ------------------------------------->>
    def nombre(self) -> str:
        return self.__nombre
        
    @property # ------------------------------------->>
    def contrasena(self) -> str:
        return self.__contrasena