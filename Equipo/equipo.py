class equipo:
    def __init__(self,id_equipo,nombre,tipo,dano,tipoDano):
        self.__id_equipo = id_equipo
        self.__nombre = nombre
        self.__tipo = tipo
        self.__dano = dano
        self.__tipoDano = tipoDano

    @property # ------------------------------------->>
    def equipo(self) -> str:
        return self.__id_equipo

    @property # ------------------------------------->>
    def nombre(self) -> str:
        return self.__nombre

    @property # ------------------------------------->>
    def tipo(self) -> str:
        return self.__tipo

    @property # ------------------------------------->>
    def raza(self) -> int:
        return self.__dano

    @property # ------------------------------------->>
    def genero(self) -> str:
        return self.__tipoDano