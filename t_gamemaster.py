class t_gamemaster:
    def __init__(self,id_gm,nombre,contrasena,historias):
        self.__id_gm = id_gm
        self.__nombre = nombre
        self.__contrasena = contrasena
        self.__historias = historias

    @property # ------------------------------------->>
    def id_gm(self) -> str:
        return self.__id_gm

    @property # ------------------------------------->>
    def nombre(self) -> str:
        return self.__nombre

    @property # ------------------------------------->>
    def contrasena(self) -> str:
        return self.__contrasena

    @property # ------------------------------------->>
    def historias(self) -> str:
        return self.__historias
