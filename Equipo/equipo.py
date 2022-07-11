class equipo:
    def __init__(self,id_equipo,nombre,tipo,dano,tipoDano):
        self.__id_equipo = id_equipo
        self.__nombre = nombre
        self.__tipo = tipo
        self.__dano = dano
        self.__tipoDano = tipoDano

    @property # ------------------------------------->>
    def id(self) -> str:
        return self.__id_equipo

    @property # ------------------------------------->>
    def nombre(self) -> str:
        return self.__nombre

    @property # ------------------------------------->>
    def tipo(self) -> str:
        return self.__tipo

    @property # ------------------------------------->>
    def dano(self) -> int:
        return self.__dano

    @property # ------------------------------------->>
    def tipoDano(self) -> str:
        return self.__tipoDano