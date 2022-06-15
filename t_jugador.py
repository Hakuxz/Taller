class t_jugador:
    def __init__(self,id_jugador,nombre,personajes):
        self.__id_jugador = id_jugador
        self.__nombre = nombre
        self.__personajes = personajes

    @property # ------------------------------------->>
    def id_jugador(self) -> str:
        return self.__id_jugador

    @property # ------------------------------------->>
    def nombre(self) -> str:
        return self.__nombre

    @property # ------------------------------------->>
    def apellido(self) -> str:
        return self.__personajes
